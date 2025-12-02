import streamlit as st

st.set_page_config(
    page_title="Geo-Mineral ID",
    page_icon="🪨",
    layout="wide"
)

# ========== CSS Biru ITB ==========
st.markdown("""
<style>
body {
    background-color: #0F1F38;
    color: white;
}
.big-title {
    font-size: 52px;
    font-weight: 800;
    color: #4DA8FF;
    text-align: center;
    margin-top: 30px;
}
.sub {
    text-align:center;
    font-size:20px;
}
.menu-card {
    background:#162C4E;
    padding:25px;
    border-radius:18px;
    color:white;
    transition: 0.3s;
}
.menu-card:hover {
    background:#1E3C69;
    transform: scale(1.03);
}
</style>
""", unsafe_allow_html=True)

# ========== Konten ==========
st.markdown("<div class='big-title'>Geo-Mineral ID</div>", unsafe_allow_html=True)
st.markdown("<p class='sub'>Sistem identifikasi mineral modern berbasis warna, densitas, nilai ekonomis, dan kegunaannya.</p>", unsafe_allow_html=True)

st.markdown("### Menu Utama:")
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("<div class='menu-card'>🔍 Identifikasi Batuan</div>", unsafe_allow_html=True)

with col2:
    st.markdown("<div class='menu-card'>💰 Hitung Nilai Ekonomis</div>", unsafe_allow_html=True)

with col3:
    st.markdown("<div class='menu-card'>🗺 Kegunaan Mineral</div>", unsafe_allow_html=True)

st.info("""
Gunakan sidebar kiri untuk berpindah halaman.
""")
