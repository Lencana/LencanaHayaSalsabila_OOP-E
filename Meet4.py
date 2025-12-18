# ===== CLASS PARENT =====
class Mhs_alumni:
    def __init__(self):
        self.tahun_lulus = 2025

    def info_lulus(self):
        print(f"Mahasiswa ini lulus pada tahun {self.tahun_lulus}")

class Mhs_aktif:
    def __init__(self):
        self.tahun_masuk = 2024

    def info_masuk(self):
        print(f"Mahasiswa ini masuk pada tahun {self.tahun_masuk}")

# ===== CLASS CHILD =====
class KTM(Mhs_aktif):
    def cetak_ktm(self):
        print("Kartu Tanda Mahasiswa telah dicetak")

class Ijazah(Mhs_alumni):
    def cetak_ijazah(self):
        print("Ijazah telah dicetak")

# Multiple inheritance (mewarisi dari dua parent)
class Beasiswa(Mhs_aktif, Mhs_alumni):
    def status_beasiswa(self):
        print("Mahasiswa ini menerima beasiswa")

# Multilevel inheritance (turunan dari class yang sudah mewarisi)
class MahasiswaPrestasi(Beasiswa):
    def prestasi(self):
        print("Mahasiswa ini berprestasi di tingkat nasional")

# ===== OBJECT & OUTPUT =====
ktm = KTM()
ijazah = Ijazah()
beasiswa = Beasiswa()
prestasi = MahasiswaPrestasi()

print("=== DATA MAHASISWA ===")
ktm.info_masuk()
ktm.cetak_ktm()

ijazah.info_lulus()
ijazah.cetak_ijazah()

beasiswa.info_masuk()
beasiswa.status_beasiswa()

prestasi.info_masuk()
prestasi.status_beasiswa()
prestasi.prestasi()
