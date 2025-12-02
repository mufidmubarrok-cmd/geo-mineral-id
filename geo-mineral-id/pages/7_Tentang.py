import streamlit as st
from utils import set_theme_fttm, animasi_masuk

set_theme_fttm()
animasi_masuk()

st.title("ℹ️ Tentang Aplikasi")
st.write("Dibuat oleh Kelompok 4 — FTTM ITB")
st.code(
"""
Abdulloh Mufid Mubarrok   16425215
Cyntia Entik Zahara       16425460
Diaz Haitham Rafhardi     16425430
Rafif Dario Kaysan        16425240
Octovia Magal             16425485
"""
)
