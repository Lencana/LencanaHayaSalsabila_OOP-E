# Class -> Motor
# Objek -> surat2, kondisi_mesin, merk, model, harga, cc, warna
# Nama : Lencana Haya Salsabila
# NIM  : 24241189

class Motor:
    def __init__(self, surat2, kondisi_mesin, merk, model, harga, cc, warna):
        self.surat2 = surat2
        self.kondisi_mesin = kondisi_mesin
        self.merk = merk
        self.model = model
        self.harga = harga
        self.cc = cc
        self.warna = warna

    def tampilkan_info(self):
        print("=== Data Motor ===")
        print(f"Surat-surat       : {self.surat2}")
        print(f"Kondisi Mesin     : {self.kondisi_mesin}")
        print(f"Merk              : {self.merk}")
        print(f"Model             : {self.model}")
        print(f"Harga             : Rp{self.harga:,}")
        print(f"CC                : {self.cc} cc")
        print(f"Warna             : {self.warna}")
        print("=====================")

# Data objek motor (contoh: Yamaha Fazzio Lux / Deluc)
motor_fazzio = Motor(
    surat2="Lengkap (STNK & BPKB)",
    kondisi_mesin="Baru",
    merk="Yamaha",
    model="Fazzio Lux",
    harga=22900000,  # harga perkiraan Rp 22,9 juta
    cc=125,
    warna="Beige"
)

# Tampilkan data motor
motor_fazzio.tampilkan_info()