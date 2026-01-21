"""
Code ini adalah contoh dari inheritance dimana class Kucing dan Anjing mewarisi sifat dari class Hewan.
inheritance adalah konsep di mana class dapat mewarisi sifat dari class lain.

super() digunakan untuk memanggil method dari parent class.
"""
class Hewan():
    nama = ""
    umur = 0
    
    def __init__(self, nama, umur):
        
        self.nama = nama
        self.umur = umur
    
    def lari(self):
        print(f"{self.nama} ini sedang lari")
    
    def makan(self):
        print(f"{self.nama} ini sedang makan")
    
    def display_info(self):
        print(f"Nama: {self.nama}, Umur: {self.umur}")

class Kucing(Hewan):
    def __init__(self, nama, umur, warna):
        super().__init__(nama, umur)
        self.warna = warna
    
class Anjing(Hewan):
    def __init__(self, nama, umur, warna):
        super().__init__(nama, umur)
        self.warna = warna

Kucingku = Kucing("Oyen", 2, "Oranye")
Anjingku = Anjing("Bintang", 3, "Hitam")

Kucingku.lari()
Anjingku.makan()

Kucingku.display_info()
Anjingku.display_info()

print(Kucingku.nama)
print(Anjingku.nama)

