import streamlit as st
import numpy as np
import plotly.graph_objects as go

st.title("🪨 Simulasi 3D Mineral — Geo-Mineral ID")

# ==========================
# Daftar Mineral & Warna HEX
# ==========================
TABEL_KLASIFIKASI = [
    ("kuning", 10, 25, "Emas (Gold)", 2180000000),
    ("putih", 10, 999, "Perak (Silver)", 26600000),
    ("perak", 10, 999, "Perak (Silver)", 26600000),
    ("keperakan", 10, 999, "Perak (Silver)", 26600000),
    ("coklat", 8, 999, "Tembaga (Copper)", 176400),
    ("merah", 8, 999, "Tembaga (Copper)", 176400),
    ("abu", 5.5, 9, "Galena (PbS)", 32800),
    ("hitam", 5, 7, "Magnetite", 1760),
    ("abu", 4, 5.5, "Hematite", 1760),
    ("kuning", 4, 8, "Pyrite (Fool’s Gold)", 10000),
    ("putih", 1, 3, "Kuarsa (Quartz)", 8000),
    ("abu", 1, 3.1, "Batu Kapur (Limestone)", 100),
    ("hitam", 3, 5, "Batu Bara (Coal)", 1830),
    ("kuning", 1, 4, "Belerang (Sulfur)", 9000),
    ("hitam", 1, 3, "Grafit (Graphite)", 60000),
    ("abu", 3.1, 3.5, "Dolomit (Dolomite)", 3500),
    ("abu", 3.5, 4, "Andesit/Basalt", 60),
]

WARNA_MINERAL = {
    "Emas (Gold)": "#FFD700",
    "Perak (Silver)": "#C0C0C0",
    "Tembaga (Copper)": "#B87333",
    "Galena (PbS)": "#808080",
    "Magnetite": "#1C1C1C",
    "Hematite": "#A9A9A9",
    "Pyrite (Fool’s Gold)": "#BDB76B",
    "Kuarsa (Quartz)": "#E0E0E0",
    "Batu Kapur (Limestone)": "#F5F5DC",
    "Batu Bara (Coal)": "#2F2F2F",
    "Belerang (Sulfur)": "#FFFF00",
    "Grafit (Graphite)": "#696969",
    "Dolomit (Dolomite)": "#DCDCDC",
    "Andesit/Basalt": "#696969"
}

# ==========================
# Input Mineral & Mode
# ==========================
mineral = st.selectbox("Pilih mineral untuk simulasi 3D:",
                       [x[3] for x in TABEL_KLASIFIKASI])

mode = st.radio("Mode Tampilan:",
                ["Simulasi Batu (default)", "Mesh Realistis (jika tersedia)"])

# ==========================
# Generate Bola Sederhana
# ==========================
def generate_sphere(radius=1, resolution=30):
    u = np.linspace(0, 2 * np.pi, resolution)
    v = np.linspace(0, np.pi, resolution)
    x = radius * np.outer(np.cos(u), np.sin(v))
    y = radius * np.outer(np.sin(u), np.sin(v))
    z = radius * np.outer(np.ones(np.size(u)), np.cos(v))
    noise = np.random.normal(0, 0.05, x.shape)
    x += noise
    y += noise
    z += noise
    return x, y, z

# ==========================
# Render 3D
# ==========================
fig = go.Figure()

if mode == "Simulasi Batu (default)":
    x, y, z = generate_sphere()
    warna = WARNA_MINERAL.get(mineral, "#AAAAAA")
    fig.add_trace(go.Mesh3d(
        x=x.flatten(),
        y=y.flatten(),
        z=z.flatten(),
        color=warna,
        opacity=0.9,
        alphahull=0
    ))
    st.write(f"Simulasi Batu untuk mineral: **{mineral}**, warna: {warna}")
else:
    st.info("Mode Mesh Realistis belum tersedia, fallback ke Simulasi Batu.")
    x, y, z = generate_sphere()
    warna = WARNA_MINERAL.get(mineral, "#AAAAAA")
    fig.add_trace(go.Mesh3d(
        x=x.flatten(),
        y=y.flatten(),
        z=z.flatten(),
        color=warna,
        opacity=0.9,
        alphahull=0
    ))

fig.update_layout(
    scene=dict(
        xaxis=dict(visible=False),
        yaxis=dict(visible=False),
        zaxis=dict(visible=False),
        aspectmode="data"
    ),
    margin=dict(l=0, r=0, b=0, t=0)
)

st.plotly_chart(fig, use_container_width=True)
