# Class -> Mobil
# Objek -> surat2, kondisi_mesin, merk, model, harga, cc, warna
# Nama : Lencana Haya Salsabila
# NIM  : 24241189

class Mobil:
    def __init__(self, surat2, kondisi_mesin, merk, model, harga, cc, warna):
        self.surat2 = surat2
        self.kondisi_mesin = kondisi_mesin
        self.merk = merk
        self.model = model
        self.harga = harga
        self.cc = cc
        self.warna = warna

    def tampilkan_info(self):
        print("=== Data Mobil ===")
        print(f"Surat-surat       : {self.surat2}")
        print(f"Kondisi Mesin     : {self.kondisi_mesin}")
        print(f"Merk              : {self.merk}")
        print(f"Model             : {self.model}")
        print(f"Harga             : Rp{self.harga:,}")
        print(f"CC                : {self.cc} cc")
        print(f"Warna             : {self.warna}")
        print("=====================")

# Data objek mobil (contoh: Toyota Yaris)
mobil_yaris = Mobil(
    surat2="Lengkap (STNK & BPKB)",
    kondisi_mesin="Bekas Terawat",
    merk="Toyota",
    model="Yaris G",
    harga=180000000,  # harga perkiraan Rp 180 juta
    cc=1500,
    warna="Merah Metalik"
)

# Tampilkan data mobil
mobil_yaris.tampilkan_info()