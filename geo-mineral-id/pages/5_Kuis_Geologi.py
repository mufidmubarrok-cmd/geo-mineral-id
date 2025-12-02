import streamlit as st
from utils import set_theme_fttm, animasi_masuk

set_theme_fttm()
animasi_masuk()
st.title("🧠 Kuis Geologi Interaktif (Step by Step)")

# ==========================
# Daftar Soal, Pilihan, Jawaban, Pembahasan
# ==========================
soal_list = [
    {
        "soal": "Mineral dengan sifat magnetik kuat?",
        "pilihan": ["Magnetite", "Hematite", "Kuarsa", "Tembaga"],
        "jawaban": "Magnetite",
        "pembahasan": "Magnetite adalah 'magnet alami' dan dapat menarik serpihan besi."
    },
    {
        "soal": "Mineral yang dijuluki Fool's Gold?",
        "pilihan": ["Pyrite", "Galena", "Hematite", "Kuarsa"],
        "jawaban": "Pyrite",
        "pembahasan": "Pyrite memiliki kilap logam dan warna keemasan, sehingga sering disangka emas."
    },
    {
        "soal": "Mineral Kuarsa digunakan sebagai patokan pada skala kekerasan Mohs, berapa nilainya?",
        "pilihan": ["7", "5", "3", "9"],
        "jawaban": "7",
        "pembahasan": "Kuarsa memiliki kekerasan 7 pada skala Mohs."
    },
    {
        "soal": "Mineral lunak berwarna hitam, tersusun dari karbon, digunakan untuk pensil?",
        "pilihan": ["Grafit", "Belerang", "Pyrite", "Kuarsa"],
        "jawaban": "Grafit",
        "pembahasan": "Grafit tersusun dari karbon, lunak, dan meninggalkan jejak hitam pada kertas."
    },
    {
        "soal": "Dua karakteristik fisik utama emas (Gold)?",
        "pilihan": ["Kelunakan dan warna", "Kelunakan dan kilap", "Kelunakan dan ductility", "Ductility dan warna"],
        "jawaban": "Kelunakan dan ductility",
        "pembahasan": "Emas sangat lunak (malleable) dan dapat ditarik menjadi kawat (ductile)."
    },
    {
        "soal": "Mineral Hematite dapat berwarna abu-abu keperakan hingga hitam, sifat fisik andal untuk identifikasi?",
        "pilihan": ["Kilap", "Magnetik", "Jejak warna", "Kekerasan"],
        "jawaban": "Jejak warna",
        "pembahasan": "Jejak warna merah-coklat hematite paling konsisten untuk identifikasi."
    },
    {
        "soal": "Batuan dari CaCO3 yang bereaksi berbuih dengan HCl?",
        "pilihan": ["Batu Kapur", "Dolomit", "Andesit", "Basalt"],
        "jawaban": "Batu Kapur",
        "pembahasan": "Batu Kapur (CaCO3) menunjukkan effervescence dengan asam klorida."
    },
    {
        "soal": "Mineral Galena memiliki keterbelahan kubik sempurna dan berat jenis tinggi. Unsur penyebab berat jenis tinggi?",
        "pilihan": ["Pb", "S", "Fe", "Cu"],
        "jawaban": "Pb",
        "pembahasan": "Galena PbS, berat jenis tinggi karena kandungan Pb (Timbal)."
    },
    {
        "soal": "Mineral logam dengan warna alami kemerahan?",
        "pilihan": ["Tembaga", "Emas", "Perak", "Magnetite"],
        "jawaban": "Tembaga",
        "pembahasan": "Tembaga logam berwarna kemerahan alami, berbeda dari logam lain."
    },
    {
        "soal": "Batuan beku ekstrusif Andesit dan Basalt dicirikan oleh tekstur?",
        "pilihan": ["Aphanitic (butiran halus)", "Phaneritic (butiran kasar)", "Vesicular", "Porphyritic"],
        "jawaban": "Aphanitic (butiran halus)",
        "pembahasan": "Andesit dan Basalt memiliki kristal kecil (aphanitic) karena pembekuan cepat."
    },
]

# ==========================
# Inisialisasi session_state
# ==========================
if "soal_index" not in st.session_state:
    st.session_state.soal_index = 0
if "skor_kuis" not in st.session_state:
    st.session_state.skor_kuis = 0
if "tampilkan_pembahasan" not in st.session_state:
    st.session_state.tampilkan_pembahasan = False

soal_idx = st.session_state.soal_index
total_soal = len(soal_list)
current_soal = soal_list[soal_idx]

# ==========================
# Tampilkan soal
# ==========================
st.subheader(f"Soal {soal_idx+1} / {total_soal}")
st.write(current_soal["soal"])
jawaban_user = st.radio("Jawaban:", current_soal["pilihan"], key=f"soal_{soal_idx}")

if st.button("Kirim Jawaban"):
    if jawaban_user == current_soal["jawaban"]:
        st.success("✅ Benar!")
        st.session_state.skor_kuis += 1
    else:
        st.error(f"❌ Salah! Jawaban benar: {current_soal['jawaban']}")
    st.info(f"Pembahasan: {current_soal['pembahasan']}")
    st.session_state.tampilkan_pembahasan = True

# ==========================
# Tombol lanjut
# ==========================
if st.session_state.tampilkan_pembahasan and soal_idx < total_soal-1:
    if st.button("➡ Lanjut Soal Berikutnya"):
        st.session_state.soal_index += 1
        st.session_state.tampilkan_pembahasan = False

# ==========================
# Skor akhir
# ==========================
if soal_idx == total_soal-1 and st.session_state.tampilkan_pembahasan:
    persen = (st.session_state.skor_kuis / total_soal) * 100
    st.subheader("📊 Kuis Selesai!")
    st.write(f"Skor: {st.session_state.skor_kuis}/{total_soal} ({persen:.2f}%)")
    if st.button("🔄 Mulai Ulang Kuis"):
        st.session_state.soal_index = 0
        st.session_state.skor_kuis = 0
        st.session_state.tampilkan_pembahasan = False
