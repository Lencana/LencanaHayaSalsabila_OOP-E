# Your first line of Python code
# multiple inheritance
# multilevel inheritance

# class grandpa (multilevel)
class Status:
    def status(self):
        print("Belum menikah")

# class parent
class MahasiswaAlumni(Status):
    def lulus(self):
        print("mahasiswa ini lulus tahun 2025")

class MahasiswaAktif:
    def masuk(self):
        print("mahasiswa ini masuk tahun 2025")

# class child
class Ktm(MahasiswaAktif):
    pass

class Ijazah(MahasiswaAlumni):
    pass

# multiple inheritance
class Beasiswa(MahasiswaAlumni, MahasiswaAktif):
    pass

# objek
Ktm = Ktm()
Ijazah = Ijazah()
Beasiswa = Beasiswa()

# pemanggilan method
Ktm.masuk()

Ijazah.lulus()
Ijazah.status()

Beasiswa.masuk()
Beasiswa.lulus()
Beasiswa.status()