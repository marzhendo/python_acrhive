set_saya = {'apel', 'mangga', 'pisang'}
set_kamu = {'pisang', 'mangga', 'semangka'}

# Intersection berfungsi untuk mengambil nilai yang sama antara set_saya dan set_kamu
print(set_saya.intersection(set_kamu))
# Union berfungsi untuk menggabungkan set_saya dan set_kamu
print(set_saya.union(set_kamu))

# Difference berfungsi untuk mengambil nilai yang berbeda antara set_saya dan set_kamu
print(set_saya.difference(set_kamu))

# Symmetric Difference berfungsi untuk mengambil nilai yang berbeda antara set_saya dan set_kamu
print(set_saya.symmetric_difference(set_kamu))


# menambahkan elemen ke dalam set
set_saya.add('semangka')
print(set_saya)

# menghapus elemen dari set
set_saya.remove('semangka')
print(set_saya)

# menghapus elemen dari set dengan menggunakan discard
set_saya.discard('semangka')
print(set_saya)

# menghapus elemen dari set dengan menggunakan pop
set_saya.pop()
print(set_saya)

# menghapus elemen dari set dengan menggunakan clear
set_saya.clear()
print(set_saya)

# menghapus elemen dari set dengan menggunakan del
set_saya = {'apel', 'mangga', 'pisang'}
del set_saya
print(set_saya)
