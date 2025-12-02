import streamlit as st

# ==========================
# INISIALISASI HISTORY
# ==========================
if "history" not in st.session_state:
    st.session_state.history = []

st.title("📜 History Analisis")
col1, col2 = st.columns(2)

with col1:
    if st.button("🗑 Hapus Semua History"):
        st.session_state.history = []
        st.success("History berhasil dihapus!")

with col2:
    if st.button("🔄 Refresh Riwayat"):
        st.success("Riwayat diperbarui")

if len(st.session_state.history) == 0:
    st.info("Belum ada riwayat")
else:
    st.subheader("Riwayat Analisis:")
    for idx, h in enumerate(st.session_state.history, start=1):
        st.write(f"{idx}. {h}")

    history_str = "\n".join(st.session_state.history)
    st.download_button(
        "💾 Download History",
        history_str,
        file_name="history.txt",
        mime="text/plain"
    )
