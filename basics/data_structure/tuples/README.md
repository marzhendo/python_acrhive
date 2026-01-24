# Python Tuples / Tuple Python

---

## 📖 Informasi / Information

### 🇮🇩 Bahasa Indonesia

**Tuple** adalah struktur data bawaan Python yang menyimpan kumpulan item secara berurutan. Tuple bersifat:

- **Immutable**: Tidak dapat diubah setelah dibuat (tidak bisa tambah, hapus, atau modifikasi)
- **Ordered**: Menjaga urutan item sesuai penyisipan
- **Indexed**: Setiap item memiliki indeks, dimulai dari 0
- **Heterogen**: Dapat menyimpan berbagai tipe data sekaligus
- **Duplikat Diizinkan**: Item yang sama dapat muncul berkali-kali
- **Hashable**: Dapat digunakan sebagai key dictionary (jika semua elemennya hashable)

**Sintaks Dasar:**

```python
nama_tuple = (item1, item2, item3)
```

### 🇬🇧 English

**Tuple** is a built-in Python data structure that stores a collection of items in order. Tuples are:

- **Immutable**: Cannot be modified after creation (no add, remove, or modify)
- **Ordered**: Maintains item order as inserted
- **Indexed**: Each item has an index, starting from 0
- **Heterogeneous**: Can store different data types together
- **Duplicates Allowed**: Same items can appear multiple times
- **Hashable**: Can be used as dictionary keys (if all elements are hashable)

**Basic Syntax:**

```python
tuple_name = (item1, item2, item3)
```

---

## 🚀 Cara Penggunaan / Usage

### 1. Membuat Tuple / Creating a Tuple

```python
# Tuple kosong / Empty tuple
empty_tuple = ()
empty_tuple = tuple()

# Tuple dengan nilai / Tuple with values
numbers = (1, 2, 3, 4, 5)
fruits = ('apple', 'banana', 'cherry')
mixed = (1, 'hello', 3.14, True)

# Tuple satu elemen (perlu koma!) / Single element tuple (comma required!)
single = (42,)      # Ini tuple / This is a tuple
not_tuple = (42)    # Ini integer! / This is an integer!

# Tuple tanpa tanda kurung / Tuple without parentheses (packing)
coordinates = -7.424550, 109.069099

# Dari list / From list
tuple_from_list = tuple([1, 2, 3])

# Dari string / From string
chars = tuple('hello')  # ('h', 'e', 'l', 'l', 'o')
```

### 2. Mengakses Elemen / Accessing Elements

```python
my_dna = ('GCT', 'GCA', 'GCG', 'GCU', 'GAA', 'GAG')

# Akses dengan indeks positif / Positive index
print(my_dna[0])   # Output: GCT
print(my_dna[2])   # Output: GCG

# Akses dengan indeks negatif / Negative index
print(my_dna[-1])  # Output: GAG (terakhir / last)
print(my_dna[-2])  # Output: GAA

# Slicing [start:end:step]
print(my_dna[1:4])    # ('GCA', 'GCG', 'GCU')
print(my_dna[:3])     # ('GCT', 'GCA', 'GCG')
print(my_dna[2:])     # ('GCG', 'GCU', 'GAA', 'GAG')
print(my_dna[::2])    # ('GCT', 'GCG', 'GAA')
print(my_dna[::-1])   # Reverse tuple
```

### 3. Tuple Unpacking

```python
# Unpacking dasar / Basic unpacking
coordinates = (-7.424550, 109.069099)
latitude, longitude = coordinates
print(f'Lat: {latitude}, Long: {longitude}')

# Unpacking dengan * / Unpacking with *
numbers = (1, 2, 3, 4, 5)
first, *middle, last = numbers
# first = 1, middle = [2, 3, 4], last = 5

# Swap values tanpa temp variable
a, b = 10, 20
a, b = b, a  # a = 20, b = 10

# Unpacking di loop
friends = (
    ('Fila', -7.221250, 109.639343),
    ('Kafi', -6.834010, 108.227631),
    ('Aedil', -6.879704, 109.125595)
)

for name, lat, long in friends:
    print(f'{name}: ({lat}, {long})')
```

### 4. Method Tuple / Tuple Methods

```python
my_dna = ('GCT', 'GCA', 'GCG', 'GCU', 'GCA', 'GAG')

# Menghitung kemunculan / Count occurrences
count = my_dna.count('GCA')  # 2

# Mencari indeks / Find index
index = my_dna.index('GCG')  # 2

# Panjang tuple / Length
length = len(my_dna)  # 6

# Min, Max (untuk tipe yang bisa dibandingkan)
numbers = (3, 1, 4, 1, 5, 9)
print(min(numbers))  # 1
print(max(numbers))  # 9
print(sum(numbers))  # 23
```

### 5. Operasi Tuple / Tuple Operations

```python
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)

# Concatenation (menghasilkan tuple baru)
combined = tuple1 + tuple2  # (1, 2, 3, 4, 5, 6)

# Repetition
repeated = tuple1 * 3  # (1, 2, 3, 1, 2, 3, 1, 2, 3)

# Membership test
print(2 in tuple1)      # True
print(7 not in tuple1)  # True

# Comparison
print((1, 2, 3) < (1, 2, 4))  # True
print((1, 2) < (1, 2, 3))    # True
```

### 6. Nested Tuple

```python
# Tuple dalam tuple / Tuple inside tuple
friends = (
    (-7.221250, 109.639343),
    (-6.834010, 108.227631),
    (-6.879704, 109.125595)
)

# Akses elemen nested / Access nested element
print(friends[0])     # (-7.221250, 109.639343)
print(friends[0][0])  # -7.221250

# Iterasi nested tuple
for lat, long in friends:
    print(f'Latitude: {lat}, Longitude: {long}')
```

### 7. Konversi / Conversion

```python
# Tuple ke List (untuk modifikasi)
my_tuple = (1, 2, 3)
my_list = list(my_tuple)
my_list.append(4)
my_tuple = tuple(my_list)  # (1, 2, 3, 4)

# List ke Tuple
my_list = [1, 2, 3]
my_tuple = tuple(my_list)

# String ke Tuple
my_string = 'hello'
my_tuple = tuple(my_string)  # ('h', 'e', 'l', 'l', 'o')
```

### 8. Tuple sebagai Dictionary Key

```python
# Tuple bisa jadi key karena immutable
locations = {
    (-7.424550, 109.069099): 'My Location',
    (-7.221250, 109.639343): 'Fila Location',
    (-6.834010, 108.227631): 'Kafi Location'
}

# Akses dengan tuple key
print(locations[(-7.424550, 109.069099)])  # My Location

# List TIDAK bisa jadi key (mutable)
# {[1, 2]: 'value'}  # TypeError: unhashable type: 'list'
```

---

## ✅ Best Practices

### 🇮🇩 Bahasa Indonesia

| #   | Praktik                               | Penjelasan                                                    |
| --- | ------------------------------------- | ------------------------------------------------------------- |
| 1   | Gunakan tuple untuk data tetap        | Koordinat, warna RGB, konstanta yang tidak berubah            |
| 2   | Tuple lebih efisien dari list         | Memory lebih kecil dan akses lebih cepat                      |
| 3   | Gunakan named tuple untuk readability | `from collections import namedtuple` untuk tuple dengan label |
| 4   | Jangan lupa koma untuk single tuple   | `(42,)` bukan `(42)`                                          |
| 5   | Gunakan unpacking                     | Lebih readable dari akses dengan indeks                       |
| 6   | Tuple sebagai return value            | Function bisa return multiple values dalam tuple              |
| 7   | Gunakan tuple untuk dictionary key    | Saat butuh key dengan multiple values                         |
| 8   | Tuple untuk data heterogen            | Cocok untuk record dengan tipe berbeda                        |

### 🇬🇧 English

| #   | Practice                            | Explanation                                             |
| --- | ----------------------------------- | ------------------------------------------------------- |
| 1   | Use tuple for fixed data            | Coordinates, RGB colors, constants that don't change    |
| 2   | Tuple is more efficient than list   | Smaller memory footprint and faster access              |
| 3   | Use named tuple for readability     | `from collections import namedtuple` for labeled tuples |
| 4   | Don't forget comma for single tuple | `(42,)` not `(42)`                                      |
| 5   | Use unpacking                       | More readable than index access                         |
| 6   | Tuple as return value               | Functions can return multiple values in a tuple         |
| 7   | Use tuple as dictionary key         | When you need composite keys                            |
| 8   | Tuple for heterogeneous data        | Good for records with different types                   |

---

## 📝 Code Examples / Contoh Kode

### Contoh 1: Koordinat GPS / GPS Coordinates

```python
my_lat = (-7.424550, 109.069099)
fila_lat = (-7.221250, 109.639343)
kafi_lat = (-6.834010, 108.227631)

# Unpacking
lat, long = my_lat
print(f'My Position: {lat}, {long}')

# Nested tuple untuk banyak lokasi
friends = (fila_lat, kafi_lat)
for location in friends:
    print(f'Friend at: {location}')
```

### Contoh 2: DNA Sequence

```python
my_dna = ('GCT', 'GCA', 'GCG', 'GCU', 'GAA', 'GAG', 'GAT', 'GAC')

# Hitung dan cari
print(f'Total codons: {len(my_dna)}')
print(f'GCA appears: {my_dna.count("GCA")} times')
print(f'GAA at index: {my_dna.index("GAA")}')

# Slice untuk sebagian sequence
first_half = my_dna[:4]
second_half = my_dna[4:]
```

### Contoh 3: Named Tuple

```python
from collections import namedtuple

# Definisikan named tuple
Location = namedtuple('Location', ['name', 'latitude', 'longitude'])

# Buat instance
my_loc = Location('Home', -7.424550, 109.069099)
fila_loc = Location('Fila', -7.221250, 109.639343)

# Akses dengan nama (lebih readable)
print(f'{my_loc.name}: ({my_loc.latitude}, {my_loc.longitude})')

# Tetap bisa akses dengan indeks
print(my_loc[0])  # Home
```

### Contoh 4: Function Return Multiple Values

```python
def get_stats(numbers):
    """Return min, max, and average as tuple."""
    return min(numbers), max(numbers), sum(numbers) / len(numbers)

data = (3, 1, 4, 1, 5, 9, 2, 6)
minimum, maximum, average = get_stats(data)
print(f'Min: {minimum}, Max: {maximum}, Avg: {average:.2f}')
```

---

## ⚠️ Common Mistakes / Kesalahan Umum

### ❌ Salah / Wrong

```python
# Lupa koma untuk single tuple
single = (42)      # Ini integer, bukan tuple!
type(single)       # <class 'int'>

# Mencoba memodifikasi tuple
my_tuple = (1, 2, 3)
my_tuple[0] = 10   # TypeError!

# Menggunakan list sebagai key (gunakan tuple)
my_dict = {[1, 2]: 'value'}  # TypeError!
```

### ✅ Benar / Correct

```python
# Tambahkan koma untuk single tuple
single = (42,)     # Ini tuple!
type(single)       # <class 'tuple'>

# Konversi ke list jika perlu modifikasi
my_tuple = (1, 2, 3)
my_list = list(my_tuple)
my_list[0] = 10
my_tuple = tuple(my_list)

# Gunakan tuple sebagai key
my_dict = {(1, 2): 'value'}  # OK!
```

---

## 🔄 Tuple vs List

| Fitur    | Tuple                   | List                        |
| -------- | ----------------------- | --------------------------- |
| Sintaks  | `(1, 2, 3)`             | `[1, 2, 3]`                 |
| Mutable  | ❌                      | ✅                          |
| Hashable | ✅                      | ❌                          |
| Dict Key | ✅                      | ❌                          |
| Memory   | Lebih kecil / Smaller   | Lebih besar / Larger        |
| Speed    | Lebih cepat / Faster    | Lebih lambat / Slower       |
| Methods  | 2 (`count`, `index`)    | 11+                         |
| Use Case | Data tetap / Fixed data | Data dinamis / Dynamic data |

---

## 📚 Referensi / References

- [Python Official Documentation - Tuples](https://docs.python.org/3/tutorial/datastructures.html#tuples-and-sequences)
- [Real Python - Python Tuples](https://realpython.com/python-lists-tuples/#python-tuples)
- [Python Named Tuples](https://docs.python.org/3/library/collections.html#collections.namedtuple)
