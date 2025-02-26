import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load Data
day_df = pd.read_csv("data/day.csv")
hour_df = pd.read_csv("data/hour.csv")

# Page Title
st.title("🚲 Dashboard Interaktif Penyewaan Sepeda")
st.markdown("### Analisis Penyewaan Sepeda Berdasarkan Waktu dan Cuaca")

# Sidebar untuk filter interaktif
st.sidebar.header("Filter Data")
selected_hour = st.sidebar.slider("Pilih Rentang Jam", 0, 23, (0, 23))

selected_weather = st.sidebar.multiselect(
    "Pilih Kategori Cuaca",
    ["Cerah", "Berawan", "Hujan Ringan", "Hujan Lebat"],
    default=["Cerah", "Berawan", "Hujan Ringan", "Hujan Lebat"],
)

selected_day_type = st.sidebar.radio("Hari Kerja atau Akhir Pekan?", ["Hari Kerja", "Akhir Pekan"])

# Mapping Cuaca
weather_map = {1: "Cerah", 2: "Berawan", 3: "Hujan Ringan", 4: "Hujan Lebat"}
day_df["weathersit"] = day_df["weathersit"].map(weather_map)
hour_df["weathersit"] = hour_df["weathersit"].map(weather_map)

# Filter Data berdasarkan pilihan user
filtered_hour_df = hour_df[
    (hour_df["hr"] >= selected_hour[0]) & (hour_df["hr"] <= selected_hour[1]) &
    (hour_df["weathersit"].isin(selected_weather))
]

filtered_day_df = day_df[day_df["weathersit"].isin(selected_weather)]

if selected_day_type == "Hari Kerja":
    filtered_hour_df = filtered_hour_df[filtered_hour_df["workingday"] == 1]
else:
    filtered_hour_df = filtered_hour_df[filtered_hour_df["workingday"] == 0]

# Analisis Penyewaan Sepeda
hourly_avg = filtered_hour_df.groupby("hr")["cnt"].mean()
weather_avg = filtered_day_df.groupby("weathersit")["cnt"].mean()

# Visualisasi Penyewaan Sepeda per Jam
st.subheader("📊 Tren Penyewaan Sepeda per Jam")
fig, ax = plt.subplots(figsize=(10, 5))
sns.lineplot(x=hourly_avg.index, y=hourly_avg.values, marker="o", color="b", ax=ax)
ax.set_title("Rata-rata Penyewaan Sepeda per Jam")
ax.set_xlabel("Jam")
ax.set_ylabel("Jumlah Penyewaan Sepeda")
ax.set_xticks(range(0, 24))
ax.grid(True)
st.pyplot(fig)

# Visualisasi Penyewaan Sepeda Berdasarkan Cuaca
st.subheader("🌦️ Penyewaan Sepeda Berdasarkan Cuaca")
fig, ax = plt.subplots(figsize=(8, 5))
sns.barplot(x=weather_avg.index, y=weather_avg.values, palette="viridis", ax=ax)
ax.set_xlabel("Cuaca")
ax.set_ylabel("Jumlah Penyewaan Sepeda")
ax.set_title("Rata-rata Penyewaan Sepeda Berdasarkan Cuaca")
st.pyplot(fig)

# Perbandingan Penyewaan di Hari Kerja vs Akhir Pekan
st.subheader("📅 Perbandingan Penyewaan di Hari Kerja vs Akhir Pekan")
day_type_avg = hour_df.groupby("workingday")["cnt"].mean()
fig, ax = plt.subplots(figsize=(6, 6))
labels = ["Akhir Pekan", "Hari Kerja"]
colors = ["#ff9999", "#66b3ff"]
ax.pie(day_type_avg, labels=labels, autopct="%1.1f%%", colors=colors, startangle=90, shadow=True)
ax.set_title("Distribusi Penyewaan Sepeda")
st.pyplot(fig)

st.markdown("---")
st.markdown("👩‍💻 **Dibuat dengan Streamlit untuk Analisis Penyewaan Sepeda** 🚴")
