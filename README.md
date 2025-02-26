# Proyek_Analisis_Data

## 📌 Deskripsi Proyek
Proyek ini bertujuan untuk menganalisis data penyewaan sepeda berdasarkan berbagai variabel seperti waktu, musim, dan hari kerja. Analisis ini kemudian divisualisasikan dalam bentuk dashboard interaktif menggunakan **Streamlit**, yang dapat diakses secara online.

---
## 📂 Struktur Direktori
```
Proyek_Analisis_Data/
├─── dashboard/
│    ├─── dashboard.py                       # Script utama untuk menjalankan Streamlit
├─── data/
│    ├─── day.csv                            # Dataset harian
│    ├─── hour.csv                           # Dataset per jam
├─── Tsamarah_Proyek_Analisis_Data.ipynb     # Google Colab untuk eksplorasi data awal
├─── requirements.txt                        # File untuk menginstal dependensi
├─── README.md                               # Dokumentasi proyek ini
└─── link_streamlit.txt                      # Link akses dashboard
```

---
## ⚙️ Instalasi dan Penggunaan

### 1️⃣ **Clone Repository**
Jika belum memiliki repository ini di lokal, clone dengan perintah berikut:
```sh
git clone https://github.com/MuthiahAinun/Proyek_Analisis_Data.git
cd Proyek_Analisis_Data
```

### 2️⃣ **Buat Virtual Environment (Opsional, tapi Disarankan)**
```sh
python -m venv env  # Untuk Windows
source env/bin/activate  # Untuk macOS/Linux
```

### 3️⃣ **Instal Dependensi**
Pastikan semua paket yang diperlukan terinstal dengan menjalankan:
```sh
pip install -r requirements.txt
```

### 4️⃣ **Jalankan Dashboard Streamlit Secara Lokal**
Untuk melihat dashboard secara lokal, jalankan perintah berikut:
```sh
streamlit run dashboard/dashboard.py
```

---
## 🚀 Deployment Streamlit Cloud
Dashboard ini telah dideploy menggunakan **Streamlit Cloud**, sehingga dapat diakses langsung tanpa harus menjalankan secara lokal.

🔗 **Akses Dashboard di sini:**
```
https://qfvz2lerzdusbu47jkpeqm.streamlit.app/
```

---
## 🔍 Analisis Data
- **Jam Paling Ramai**: Penyewaan sepeda tertinggi terjadi pada **pukul 17:00** di hari kerja dengan rata-rata **461 sepeda**.
- **Jam Paling Sepi**: Penyewaan sepeda terendah terjadi pada **pukul 4:00** di akhir pekan dengan rata-rata **6 sepeda**.
- **Cuaca dengan Penyewaan Tertinggi**: Cuaca **Cerah** memiliki jumlah penyewaan tertinggi, yaitu **4877 sepeda**.
- **Cuaca dengan Penyewaan Terendah**: Cuaca **Hujan** memiliki jumlah penyewaan terendah, yaitu **1803 sepeda**.

---
## 🎯 Fitur Dashboard
✅ **Visualisasi Interaktif**
- Grafik jumlah penyewaan berdasarkan jam, hari, dan cuaca.
- Perbandingan penyewaan di hari kerja dan akhir pekan.

✅ **Clustering Manual**
- Pembagian jam penyewaan ke dalam beberapa kelompok untuk analisis pola pengguna.

✅ **Akses Mudah**
- Dapat diakses melalui web tanpa perlu menginstal aplikasi tambahan.

---
## 🤝 Kontribusi
Jika ingin berkontribusi dalam proyek ini, silakan lakukan **fork**, buat perubahan yang diperlukan, lalu ajukan **pull request**!

📧 Hubungi saya melalui [GitHub](https://github.com/MuthiahAinun) jika ada pertanyaan.

---

