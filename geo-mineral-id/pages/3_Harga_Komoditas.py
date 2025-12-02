import streamlit as st

# ==========================
# INISIALISASI HISTORY
# ==========================
if "history" not in st.session_state:
    st.session_state.history = []

st.title("💹 Hitung Nilai Ekonomis Mineral")

DAFTAR_MINERAL = [
    "Emas (Gold)", "Perak (Silver)", "Tembaga (Copper)", "Nikel (Nickel)",
    "Galena (PbS)", "Magnetite", "Hematite", "Pyrite (Fool’s Gold)",
    "Kuarsa (Quartz)", "Batu Kapur (Limestone)", "Batu Bara (Coal)",
    "Belerang (Sulfur)", "Grafit (Graphite)", "Dolomit (Dolomite)",
    "Andesit/Basalt"
]

HARGA_JENIS = {
    "emas": 2180000000, "perak": 26600000, "tembaga": 176400, "galena": 32800,
    "magnetite": 1760, "hematite": 1760, "pyrite": 10000, "kuarsa": 8000,
    "batu kapur": 100, "batu bara": 1830, "belerang": 9000, "grafit": 60000,
    "dolomit": 3500, "andesit": 60, "basalt": 60
}

def dapatkan_harga(nama_mineral: str):
    nama = nama_mineral.lower().replace("(", "").replace(")", "")
    for key in HARGA_JENIS:
        if key in nama:
            return HARGA_JENIS[key]
    return 0

jumlah = st.number_input("Jumlah jenis mineral yang ingin dihitung:", min_value=1, step=1)
daftar_mineral = []

for i in range(jumlah):
    st.subheader(f"Mineral ke-{i+1}")
    mineral = st.selectbox(f"Pilih Mineral ke-{i+1}:", DAFTAR_MINERAL, key=f"mineral_{i}")
    berat = st.number_input(f"Berat (kg) {mineral}:", min_value=0.0001, step=0.01, key=f"berat_{i}")
    harga = dapatkan_harga(mineral)
    total = berat * harga
    daftar_mineral.append({"mineral": mineral, "berat": berat, "harga": harga, "total": total})
    st.write(f"Harga per kg: Rp {format(harga,',')}")
    st.write(f"Total nilai: Rp {format(int(total),',')}")

if st.button("Hitung Total Semua Mineral"):
    total_semua = sum([m["total"] for m in daftar_mineral])
    st.success(f"💰 Total nilai semua mineral = Rp {format(int(total_semua),',')}")
    
    # Simpan ke history
    entry = "Hitung Nilai Ekonomis:\n"
    for m in daftar_mineral:
        entry += f"- {m['mineral']}: {m['berat']} kg × Rp {format(m['harga'],',')} = Rp {format(int(m['total']),',')}\n"
    entry += f"Total Nilai = Rp {format(int(total_semua),',')}"
    st.session_state.history.append(entry)
