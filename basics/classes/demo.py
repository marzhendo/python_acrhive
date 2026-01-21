"""
Di python ada beberapa cara untuk menggunakan atribut dalam class.
Sebelumnya class ibarat seperti blue print sedangkan objek atau
instances adalah produk yang dibuat dari class.
"""

# Cara Deklarasi sebuah class
# class nama_class:
#     atribut = nilai
#     def __init__(self, param):  <-- (opsional)
#         self.param = param    
# contoh implementasinya:
class Mahasiswa:
    nama = ""
    nim = ""
    umur = 0
    jurusan = ""
    def __init__(self, nama, nim, umur, jurusan):
        self.nama = nama
        self.nim = nim
        self.umur = umur
        self.jurusan  = jurusan
    def display_info(self):
        print(f'Mahasiswa dengan nama {self.nama}, dan nim {self.nim}, dan umur {self.umur}, dan jurusan {self.jurusan}.')
    
# Deklarasi instance dengan memanfaatkan method __init__ lebih efisien
marzhendo = Mahasiswa("Marzhendo", "102124020", 19, "Teknik Informatika")
print(vars(marzhendo))
marzhendo.display_info()

# Cara lain 
class Kucing():
    nama = ""
    jenis = ""
    umur = ""

kucingku = Kucing()
kucingku.nama = "Oyen"
kucingku.jenis = "British Shorthair"
kucingku.umur = 1
print(vars(kucingku))
print(f'Kucingku namanya {kucingku.nama}. Jenisnya {kucingku.jenis}, terus umurnya baru {kucingku.umur}!')