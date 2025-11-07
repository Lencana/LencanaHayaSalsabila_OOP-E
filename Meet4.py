# Parent Class
class Orang:
    def __init__(self, nama, usia):
        self.nama = nama
        self.usia = usia
    
    def sapa(self):
        print(f"Halo, nama saya {self.nama}")

# Child Class 1 - Dosen
class Dosen(Orang):
    def __init__(self, nama, usia, nidn, mata_kuliah):
        super().__init__(nama, usia)
        self.nidn = nidn
        self.mata_kuliah = mata_kuliah
    
    def mengajar(self):
        print(f"{self.nama} sedang mengajar {self.mata_kuliah}.")
    
    def sapa(self):
        print(f"Halo, saya Dosen {self.nama}")

# Child Class 2 - Mahasiswa
class Mahasiswa(Orang):
    def __init__(self, nama, usia, nim, jurusan):
        super().__init__(nama, usia)
        self.nim = nim
        self.jurusan = jurusan
    
    def belajar(self):
        print(f"{self.nama} sedang belajar di jurusan {self.jurusan}.")
    
    def sapa(self):
        print(f"Halo, saya Mahasiswa {self.nama}")

# --- Membuat Objek ---

# 1. Data Dosen
dosen_Edy = Dosen(
    nama="Edy",
    usia=17,
    nidn="123456",
    mata_kuliah="Pemrograman Berorientasi Objek"
)

# 2. Data Mahasiswa
mahasiswa_Lencana = Mahasiswa(
    nama="Lencana",
    usia=20,
    nim="24241189",
    jurusan="Pendidikan Teknologi Informasi"
)

# --- Menampilkan Output ---

print("=== Data Dosen ===")
print(f"Nama: {dosen_Edy.nama}")
print(f"Usia: {dosen_Edy.usia}")
print(f"NIDN: {dosen_Edy.nidn}")
print(f"Mata Kuliah: {dosen_Edy.mata_kuliah}")
dosen_Edy.mengajar()
dosen_Edy.sapa()

print("=== Data Mahasiswa ===")
print(f"Nama: {mahasiswa_Lencana.nama}")
print(f"Usia: {mahasiswa_Lencana.usia}")
print(f"NIM: {mahasiswa_Lencana.nim}")
print(f"Jurusan: {mahasiswa_Lencana.jurusan}")
mahasiswa_Lencana.belajar()
mahasiswa_Lencana.sapa()
