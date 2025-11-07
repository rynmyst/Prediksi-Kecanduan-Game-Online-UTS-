
# Prediksi Kecanduan Game Online

## 1. File Structures

E:/UTS-PembelajaranMesin/
├── dataset
│   └── online_gaming_behavior_dataset.csv
├── model_ensemble.pkl
├── model_kmeans.pkl
├── preprocessing.pkl
├── README.md
├── streamlit_app.py
├── main_final.ipynb
└── requirements.txt


## 2. Project Work Cycle

1. **Data Preprocessing**
   - Mengumpulkan dataset perilaku pemain.
   - Membersihkan dan menormalisasi data.
   - Melakukan encoding untuk variabel kategori (`Gender`, `GameGenre`).

2. **Exploratory Data Analysis (EDA)**
   - Membuat visualisasi distribusi fitur seperti `PlayTimeHours`.
   - Analisis pola perilaku pemain.

3. **Modeling**
   - KMeans Clustering untuk mengelompokkan pemain berdasarkan perilaku bermain.
   - Ensemble Model untuk prediksi kategori pemain: `Casual`, `Active`, `Potentially Addicted`.
   - Feature Engineering: `Total Engagement` dan `Purchase Intensity`.

4. **Dashboard / Streamlit App**
   - Input data pemain melalui form.
   - Menampilkan hasil prediksi kategori dan cluster.
   - Visualisasi fitur pemain.
   - Histogram `PlayTimeHours` dan scatter plot cluster (opsional).
   - Confusion matrix model ensemble (opsional).

> **Catatan:** Langkah 1–3 dilakukan di `main_final.ipynb`, sedangkan langkah 4 berada di `streamlit_app.py`.


## 3. Getting Started

### a. `main_final.ipynb`
1. Download proyek ini.
2. Buka IDE favorit kamu (Jupyter Notebook / VSCode / Google Colab).
3. Upload dan buka file `main_final.ipynb`.
4. Jalankan seluruh cell untuk preprocessing, EDA, dan training model.
5. Simpan model dengan `joblib`:  
   - `model_ensemble.pkl`  
   - `model_kmeans.pkl`  
   - `preprocessing.pkl`

### b. `streamlit_app.py`
1. Download proyek ini.
2. Pastikan Python 3.11+ terinstall.
3. Install semua library yang dibutuhkan:

```
pip install -r requirements.txt
```

4. Pastikan file `.pkl` dan folder `dataset` tetap di lokasi yang sama, karena dibutuhkan aplikasi.

5. Jalankan Streamlit:

```
streamlit run streamlit_app.py
```

6. Aplikasi akan terbuka di browser. Masukkan data pemain di form untuk melihat:

   * Cluster KMeans
   * Prediksi Ensemble Model
   * Visualisasi Total Engagement & Purchase Intensity
   * Histogram PlayTimeHours
   * Scatter plot cluster (jika dataset tersedia)
   * Confusion matrix (jika data test tersedia)

---

## 4. Variabel Penting

| Variabel                  | Deskripsi                                                                 |
| ------------------------- | ------------------------------------------------------------------------- |
| Age                       | Umur pemain (tahun)                                                       |
| Gender                    | Jenis kelamin pemain (Male/Female)                                        |
| GameGenre                 | Genre game favorit (Action, Strategy, RPG, Sports, Simulation)            |
| PlayTimeHours             | Total jam bermain per minggu                                              |
| SessionsPerWeek           | Jumlah sesi bermain per minggu                                            |
| AvgSessionDurationMinutes | Rata-rata durasi tiap sesi bermain (menit)                                |
| InGamePurchases           | Jumlah pembelian dalam game                                               |
| Total Engagement          | Kombinasi `PlayTimeHours`, `SessionsPerWeek`, `AvgSessionDurationMinutes` |
| Purchase Intensity        | `InGamePurchases` × `SessionsPerWeek`                                     |

> **Catatan:** `PlayTimeHours` berkorelasi dengan `SessionsPerWeek` dan `AvgSessionDurationMinutes`, karena jam bermain total = jumlah sesi × durasi rata-rata.

---

## 5. Deployment & Demo

* **Local:** Jalankan Streamlit seperti di atas.
* **Web/Cloud:** Bisa deploy di [Streamlit Cloud](https://streamlit.io/cloud) atau platform serupa.
* **GitHub Repository:** Pastikan kode rapi, terdokumentasi, dan sertakan README ini.

---

## 6. Contoh Input dan Output

**Input:**

* Age: 20
* Gender: Male
* GameGenre: Action
* PlayTimeHours: 5
* SessionsPerWeek: 2
* AvgSessionDurationMinutes: 30
* InGamePurchases: 0

**Output Prediksi:**

* Cluster KMeans: Casual
* Prediksi Ensemble Model: Casual
* Total Engagement: 2.33
* Purchase Intensity: 0

**Interpretasi:** Pemain ini memiliki jam bermain rendah dan sesi bermain jarang, sehingga dikategorikan sebagai pemain casual.


