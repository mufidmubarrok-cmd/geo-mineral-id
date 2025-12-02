import streamlit as st

# ==========================
# DATA DASAR SISTEM
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

# ==========================
# INISIALISASI HISTORY
# ==========================
if "history" not in st.session_state:
    st.session_state.history = []

# ==========================
# STREAMLIT UI
# ==========================
st.title("🔍 Identifikasi Mineral")

jumlah = st.number_input("Jumlah mineral yang ingin diidentifikasi:", min_value=1, step=1)
hasil_identifikasi = []

for i in range(jumlah):
    st.subheader(f"Mineral ke-{i+1}")
    warna = st.selectbox(f"Warna dominan mineral ke-{i+1}:", 
                         ["kuning","putih","perak","keperakan","coklat","merah","abu","hitam"], key=f"warna_{i}")
    berat = st.number_input(f"Berat (kg) mineral ke-{i+1}:", min_value=0.0001, step=0.01, key=f"berat_{i}")
    volume = st.number_input(f"Volume (L) mineral ke-{i+1}:", min_value=0.0001, step=0.01, key=f"volume_{i}")
    
    kepadatan = berat / volume
    st.write(f"**Kepadatan:** {round(kepadatan,2)} kg/L")

    if st.button(f"Identifikasi Mineral ke-{i+1}", key=f"ident_{i}"):
        hasil = []
        for w, dmin, dmax, nama, harga in TABEL_KLASIFIKASI:
            if w == warna and dmin <= kepadatan <= dmax:
                hasil.append(nama)
        
        if hasil:
            st.success("Kemungkinan mineral:")
            for h in hasil:
                st.write(f"- {h}")
        else:
            alternatif = []
            for w, dmin, dmax, nama, harga in TABEL_KLASIFIKASI:
                if w == warna or (dmin*0.9 <= kepadatan <= dmax*1.1):
                    alternatif.append(nama)
            if alternatif:
                st.info("Tidak ditemukan yang tepat, kemungkinan mendekati:")
                for a in alternatif:
                    st.write(f"- {a}")
            else:
                st.error("Mineral tidak ditemukan, butuh data lebih lengkap.")
        
        # Simpan ke history
        entry = f"Identifikasi Mineral ke-{i+1}: Warna {warna}, Berat {berat} kg, Volume {volume} L, Kepadatan {round(kepadatan,2)} → Kemungkinan: {', '.join(hasil if hasil else alternatif)}"
        st.session_state.history.append(entry)
