import streamlit as st
from utils import set_theme_fttm, animasi_masuk

# ==========================
# Tema & animasi
# ==========================
set_theme_fttm()
animasi_masuk()
st.title("💎 Kegunaan Mineral")

# ==========================
# Data mineral dan kegunaannya
# ==========================
DAFTAR_MINERAL = {
    "Emas (Gold)": "Digunakan untuk perhiasan, elektronik, dan cadangan devisa.",
    "Perak (Silver)": "Digunakan untuk perhiasan, fotografi, elektronik, dan koin.",
    "Tembaga (Copper)": "Digunakan dalam kabel listrik, pipa, dan konstruksi.",
    "Nikel (Nickel)": "Digunakan untuk stainless steel, baterai, dan pelapis logam.",
    "Galena (PbS)": "Sumber utama timbal, digunakan dalam baterai dan pelindung radiasi.",
    "Magnetite": "Digunakan sebagai bijih besi, industri baja, dan magnet.",
    "Hematite": "Bijih besi, digunakan dalam baja dan cat pigmen.",
    "Pyrite (Fool’s Gold)": "Digunakan sebagai sumber sulfur, pembuatan asam sulfat.",
    "Kuarsa (Quartz)": "Digunakan dalam gelas, elektronik, jam, dan bahan bangunan.",
    "Batu Kapur (Limestone)": "Digunakan dalam semen, pupuk, dan konstruksi.",
    "Batu Bara (Coal)": "Sumber energi untuk listrik dan industri.",
    "Belerang (Sulfur)": "Pembuatan pupuk, bahan kimia, dan obat-obatan.",
    "Grafit (Graphite)": "Digunakan dalam pensil, pelumas, dan baterai.",
    "Dolomit (Dolomite)": "Digunakan dalam semen, konstruksi, dan industri kaca.",
    "Andesit/Basalt": "Bahan konstruksi dan pengeras jalan."
}

# ==========================
# Pilih mineral
# ==========================
mineral = st.selectbox("Pilih mineral:", list(DAFTAR_MINERAL.keys()))

# ==========================
# Tampilkan kegunaan
# ==========================
st.subheader(f"Kegunaan {mineral}:")
st.write(DAFTAR_MINERAL[mineral])
