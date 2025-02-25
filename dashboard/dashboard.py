import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load Data
day_df = pd.read_csv("Proyek_Analisis_Data/data/day.csv")
hour_df = pd.read_csv("Proyek_Analisis_Data/data/hour.csv")

# Page Title
st.title("🚲 Dashboard Interaktif Penyewaan Sepeda")
st.markdown("### Analisis Penyewaan Sepeda Berdasarkan Waktu dan Musim")

# Sidebar untuk filter interaktif
st.sidebar.header("Filter Data")
selected_hour = st.sidebar.slider("Pilih Jam", 0, 23, (0, 23))
selected_season = st.sidebar.selectbox("Pilih Musim", ["Winter", "Spring", "Summer", "Fall"])
selected_day_type = st.sidebar.radio("Hari Kerja atau Akhir Pekan?", ["Hari Kerja", "Akhir Pekan"])

# Mapping Season
season_map = {1: "Winter", 2: "Spring", 3: "Summer", 4: "Fall"}
day_df['season'] = day_df['season'].map(season_map)

# Filter Data berdasarkan pilihan user
filtered_hour_df = hour_df[(hour_df['hr'] >= selected_hour[0]) & (hour_df['hr'] <= selected_hour[1])]
filtered_day_df = day_df[day_df['season'] == selected_season]

if selected_day_type == "Hari Kerja":
    filtered_hour_df = filtered_hour_df[filtered_hour_df['workingday'] == 1]
else:
    filtered_hour_df = filtered_hour_df[filtered_hour_df['workingday'] == 0]

# Analisis Penyewaan Sepeda
hourly_avg = filtered_hour_df.groupby('hr')['cnt'].mean()
season_avg = filtered_day_df.groupby('season')['cnt'].mean()

# Visualisasi Penyewaan Sepeda per Jam
st.subheader("📊 Tren Penyewaan Sepeda per Jam")
fig, ax = plt.subplots(figsize=(10, 5))
sns.lineplot(x=hourly_avg.index, y=hourly_avg.values, marker='o', color='b', ax=ax)
ax.set_title("Rata-rata Penyewaan Sepeda per Jam")
ax.set_xlabel("Jam")
ax.set_ylabel("Jumlah Penyewaan Sepeda")
ax.set_xticks(range(0, 24))
ax.grid(True)
st.pyplot(fig)

# Visualisasi Penyewaan Sepeda Berdasarkan Musim
st.subheader("🌦️ Penyewaan Sepeda Berdasarkan Musim")
fig, ax = plt.subplots(figsize=(8, 5))
sns.barplot(x=season_avg.index, y=season_avg.values, palette="viridis", ax=ax)
ax.set_xlabel("Musim")
ax.set_ylabel("Jumlah Penyewaan Sepeda")
ax.set_title("Rata-rata Penyewaan Sepeda Berdasarkan Musim")
st.pyplot(fig)

# Perbandingan Penyewaan di Hari Kerja vs Akhir Pekan
st.subheader("📅 Perbandingan Penyewaan di Hari Kerja vs Akhir Pekan")
day_type_avg = hour_df.groupby('workingday')['cnt'].mean()
fig, ax = plt.subplots(figsize=(6, 6))
labels = ["Akhir Pekan", "Hari Kerja"]
colors = ["#ff9999", "#66b3ff"]
ax.pie(day_type_avg, labels=labels, autopct='%1.1f%%', colors=colors, startangle=90, shadow=True)
ax.set_title("Distribusi Penyewaan Sepeda")
st.pyplot(fig)

st.markdown("---")
st.markdown("👩‍💻 **Dibuat dengan Streamlit untuk Analisis Penyewaan Sepeda** 🚴")
