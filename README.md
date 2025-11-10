Baik, berikut versi **README.md tanpa emoji** dan sudah diformat **supaya tampil rapi di GitHub** (bisa langsung kamu copy–paste ke file `README.md` di proyekmu):

---

```markdown
# Prediksi Kecanduan Game Online

## 1. File Structures
```

UTS-PembelajaranMesin/
│
├── dataset/
│   └── online_gaming_behavior_dataset.csv
│
├── model_ensemble.pkl
├── model_kmeans.pkl
├── preprocessing.pkl
│
├── main_final.ipynb
├── streamlit_app.py
├── requirements.txt
└── README.md

````

---

## 2. Alur Pengerjaan Proyek

1. **Data Preprocessing**
   - Mengumpulkan dan membersihkan dataset perilaku pemain game.
   - Normalisasi fitur numerik agar model tidak bias.
   - Melakukan encoding pada variabel kategori seperti `Gender` dan `GameGenre`.

2. **Exploratory Data Analysis (EDA)**
   - Membuat histogram, heatmap, dan analisis korelasi antar fitur.
   - Mengidentifikasi pola perilaku bermain berdasarkan waktu dan interaksi pemain.

3. **Modeling**
   - Menggunakan algoritma **K-Means Clustering** untuk melakukan segmentasi pemain berdasarkan perilaku bermain.
   - Menggabungkan **Decision Tree**, **Random Forest**, dan **Deep MLP** dalam model **Ensemble Learning**.
   - Menambahkan fitur turunan seperti `TotalEngagement` dan `PurchaseIntensity` untuk memperkaya data.

4. **Deployment (Dashboard Streamlit)**
   - Input data pemain secara interaktif.
   - Menampilkan hasil prediksi cluster dan kategori kecanduan.
   - Visualisasi fitur pemain, histogram waktu bermain, dan confusion matrix.

Catatan:  
Langkah 1–3 dilakukan di file `main_final.ipynb`,  
sedangkan langkah 4 berada di `streamlit_app.py`.

---

## 3. Cara Menjalankan Proyek

### A. Menjalankan Notebook
1. Buka **VSCode** atau **Jupyter Notebook**.
2. Jalankan file:
   ```bash
   main_final.ipynb
````

3. Tunggu proses training model selesai hingga file `.pkl` tersimpan otomatis.

### B. Menjalankan Dashboard Streamlit

1. Pastikan semua library sudah terinstal:

   ```bash
   pip install -r requirements.txt
   ```
2. Jalankan Streamlit melalui terminal:

   ```bash
   python -m streamlit run streamlit_app.py
   ```
3. Aplikasi akan terbuka otomatis di browser dengan alamat:

   ```
   http://localhost:8501
   ```

---

## 4. Fitur Utama Aplikasi

* Form input interaktif (usia, genre game, jam bermain, pembelian, dan lainnya)
* Prediksi **kategori kecanduan**: `Casual`, `Active`, atau `Potentially Addicted`
* Visualisasi interaktif:

  * Histogram waktu bermain
  * Scatter plot hasil clustering
  * Confusion matrix dummy

---

## 5. Teknologi yang Digunakan

| Komponen                | Teknologi                                                |
| ----------------------- | -------------------------------------------------------- |
| Bahasa Pemrograman      | Python 3.11.9                                            |
| Framework Visualisasi   | Streamlit                                                |
| Library Utama           | Pandas, NumPy, Scikit-learn, Matplotlib, Seaborn, Joblib |
| Lingkungan Pengembangan | Visual Studio Code (Jupyter Notebook Extension)          |

---

## 6. Sumber Dataset

Dataset diperoleh dari Kaggle:
[Predict Online Gaming Behavior Dataset](https://www.kaggle.com/datasets/rabieelkharoua/predict-online-gaming-behavior-dataset)

---

## 7. Hasil Model

* Akurasi Ensemble Model: ±99.9%
* Cross Validation: 99.94% ± 0.01
* Kategori Output: Casual, Active, Potentially Addicted

---

## 8. Pengembang

Nama: Ryan Christian Aruan
Proyek: UTS Pembelajaran Mesin – Tahun Ajaran 2025/2026

---

“Data bisa menipu, tetapi pola perilaku tidak pernah berbohong.”

````

---

### Petunjuk:
- Simpan teks di atas ke dalam file `README.md`.
- Pastikan bagian blok kode (yang diapit oleh ``` ) tidak dihapus.
- Jika kamu buka di GitHub, tampilannya akan otomatis rapi seperti format folder dan tabel.
````
