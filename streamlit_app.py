# streamlit_app_final.py
import streamlit as st
import pandas as pd
import joblib
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix
import numpy as np

# =========================
# Load Model & Preprocessing
# =========================
kmeans = joblib.load("model_kmeans.pkl")
ensemble = joblib.load("model_ensemble.pkl")
preproc = joblib.load("preprocessing.pkl")
scaler = preproc['scaler']
label_encoders = preproc['encoders']

num_cols = ['Age','PlayTimeHours','SessionsPerWeek','AvgSessionDurationMinutes','InGamePurchases']
features_cluster = ['PlayTimeHours','SessionsPerWeek','AvgSessionDurationMinutes','InGamePurchases','TotalEngagement']

# =========================
# Streamlit UI
# =========================
st.set_page_config(page_title="Prediksi Kecanduan Game Online", layout="wide")
st.title("Prediksi Potensi Kecanduan Game Online")
st.write("Masukkan data pemain untuk melihat kategori kecanduan dan cluster-nya.")

# Input form
with st.form("input_form"):
    age = st.number_input("Age", min_value=10, max_value=70, value=20)
    gender = st.selectbox("Gender", ["Male", "Female"])
    genre = st.selectbox("GameGenre", ["Action","Strategy","RPG","Sports","Simulation"])
    play_hours = st.number_input("PlayTimeHours per Week", min_value=0, max_value=100, value=15)
    sessions = st.number_input("SessionsPerWeek", min_value=0, max_value=50, value=9)
    avg_duration = st.number_input("AvgSessionDurationMinutes", min_value=0, max_value=300, value=120)
    purchases = st.number_input("InGamePurchases", min_value=0, max_value=20, value=3)
    submitted = st.form_submit_button("Prediksi")

if submitted:
    df_new = pd.DataFrame([{
        'Age': age, 'Gender': gender, 'GameGenre': genre,
        'PlayTimeHours': play_hours, 'SessionsPerWeek': sessions,
        'AvgSessionDurationMinutes': avg_duration, 'InGamePurchases': purchases
    }])

    # Encoding kategori
    for col in ['Gender','GameGenre']:
        df_new[col] = label_encoders[col].transform(df_new[col])

    # Normalisasi numerik
    df_new[num_cols] = scaler.transform(df_new[num_cols])

    # Feature engineering
    df_new["TotalEngagement"] = (df_new["PlayTimeHours"] + df_new["SessionsPerWeek"] + df_new["AvgSessionDurationMinutes"])/3
    df_new["PurchaseIntensity"] = df_new["InGamePurchases"] * df_new["SessionsPerWeek"]

    # Prediksi
    cluster = kmeans.predict(df_new[features_cluster])[0]
    pred = ensemble.predict(df_new)[0]
    mapping = {0:'Casual',1:'Active',2:'Potentially_Addicted'}

    st.subheader("Hasil Prediksi")
    st.write(f"Cluster (KMeans): **{mapping.get(cluster)}**")
    st.write(f"Prediksi Ensemble Model: **{mapping.get(pred)}**")

    # Visualisasi fitur
    st.subheader("Visualisasi Fitur Pemain")
    fig, ax = plt.subplots(figsize=(4,3))
    sns.barplot(x=["TotalEngagement","PurchaseIntensity"], 
                y=[df_new["TotalEngagement"].iloc[0], df_new["PurchaseIntensity"].iloc[0]], ax=ax)
    ax.set_ylabel("Nilai Ternormalisasi")
    plt.tight_layout()
    st.pyplot(fig, use_container_width=False)

# =========================
# Histogram PlayTimeHours
# =========================
st.subheader("Distribusi Jam Bermain (PlayTimeHours)")
try:
    df_data = pd.read_csv("dataset/online_gaming_behavior_dataset.csv")
    fig, ax = plt.subplots(figsize=(5,3))
    sns.histplot(df_data["PlayTimeHours"], kde=True, bins=30, color='skyblue', ax=ax)
    ax.set_xlabel("Jam Bermain")
    ax.set_ylabel("Jumlah Pemain")
    plt.tight_layout()
    st.pyplot(fig, use_container_width=False)
except FileNotFoundError:
    st.warning("Dataset asli tidak ditemukan, histogram tidak dapat ditampilkan.")

# =========================
# Scatter Cluster KMeans
# =========================
st.subheader("Visualisasi Cluster KMeans")
try:
    df_model = pd.read_csv("dataset/online_gaming_behavior_dataset.csv")
    for col in num_cols:
        if col not in df_model.columns:
            df_model[col] = 20
    df_model[num_cols] = scaler.transform(df_model[num_cols])
    df_model["TotalEngagement"] = (df_model["PlayTimeHours"] + df_model["SessionsPerWeek"] + df_model["AvgSessionDurationMinutes"])/3
    df_model["PurchaseIntensity"] = df_model["InGamePurchases"] * df_model["SessionsPerWeek"]
    df_model['Cluster'] = kmeans.predict(df_model[features_cluster])
    
    fig, ax = plt.subplots(figsize=(5,3))
    sns.scatterplot(x='PlayTimeHours', y='SessionsPerWeek', hue='Cluster', data=df_model, palette='Set2', ax=ax)
    ax.set_title("Scatter Plot Cluster KMeans")
    plt.tight_layout()
    st.pyplot(fig, use_container_width=False)
except FileNotFoundError:
    st.warning("Dataset asli tidak ditemukan, scatter plot cluster tidak dapat ditampilkan.")

# =========================
# Confusion Matrix Dummy
# =========================
st.subheader("Confusion Matrix Model Ensemble (Dummy)")
try:
    y_true = np.random.randint(0,3,size=50)
    y_pred = np.random.randint(0,3,size=50)
    cm = confusion_matrix(y_true, y_pred)
    fig, ax = plt.subplots(figsize=(4,3))
    sns.heatmap(cm, annot=True, fmt="d", cmap="Blues", ax=ax)
    ax.set_xlabel("Prediksi")
    ax.set_ylabel("Aktual")
    plt.tight_layout()
    st.pyplot(fig, use_container_width=False)
except Exception as e:
    st.warning(f"Confusion matrix tidak dapat ditampilkan: {e}")
