# Random digunakan untuk menghasilkan angka acak
import random

# Random.choice digunakan untuk memilih item acak dari list
# dibawah ini akan memilih 3 item acak dari list buah (bisa duplikat)
buah = ['apel', 'pisang', 'mangga', 'semangka', 'durian']
hasil = random.choices(buah, k = 3)
print(hasil)
print("Contoh Random tanpa duplikat")
hasil = random.sample(buah, k = 3)
print(hasil)
print("Contoh ambil salah satu dengan acak")
hasil = random.choice(buah)
print(hasil)