# Python List / Daftar Python

---

## 📖 Informasi / Information

### 🇮🇩 Bahasa Indonesia

**List** adalah struktur data bawaan Python yang menyimpan kumpulan item secara berurutan. List bersifat:

- **Mutable**: Dapat diubah setelah dibuat (tambah, hapus, modifikasi)
- **Ordered**: Menjaga urutan item sesuai penyisipan
- **Indexed**: Setiap item memiliki indeks, dimulai dari 0
- **Heterogen**: Dapat menyimpan berbagai tipe data sekaligus
- **Duplikat Diizinkan**: Item yang sama dapat muncul berkali-kali

**Sintaks Dasar:**

```python
nama_list = [item1, item2, item3]
```

### 🇬🇧 English

**List** is a built-in Python data structure that stores a collection of items in order. Lists are:

- **Mutable**: Can be modified after creation (add, remove, modify)
- **Ordered**: Maintains item order as inserted
- **Indexed**: Each item has an index, starting from 0
- **Heterogeneous**: Can store different data types together
- **Duplicates Allowed**: Same items can appear multiple times

**Basic Syntax:**

```python
list_name = [item1, item2, item3]
```

---

## 🚀 Cara Penggunaan / Usage

### 1. Membuat List / Creating a List

```python
# List kosong / Empty list
empty_list = []
empty_list = list()

# List dengan nilai / List with values
numbers = [1, 2, 3, 4, 5]
fruits = ['apple', 'banana', 'cherry']
mixed = [1, 'hello', 3.14, True]

# List dari string / List from string
chars = list('hello')  # ['h', 'e', 'l', 'l', 'o']

# List dari range / List from range
nums = list(range(5))  # [0, 1, 2, 3, 4]
```

### 2. Mengakses Elemen / Accessing Elements

```python
fruits = ['apple', 'banana', 'cherry', 'date', 'elderberry']

# Akses dengan indeks positif / Positive index
print(fruits[0])   # Output: apple
print(fruits[2])   # Output: cherry

# Akses dengan indeks negatif / Negative index
print(fruits[-1])  # Output: elderberry (terakhir / last)
print(fruits[-2])  # Output: date

# Slicing [start:end:step]
print(fruits[1:4])    # ['banana', 'cherry', 'date']
print(fruits[:3])     # ['apple', 'banana', 'cherry']
print(fruits[2:])     # ['cherry', 'date', 'elderberry']
print(fruits[::2])    # ['apple', 'cherry', 'elderberry']
print(fruits[::-1])   # Reverse list
```

### 3. Menambah Elemen / Adding Elements

```python
fruits = ['apple', 'banana']

# Menambah di akhir / Add at the end
fruits.append('cherry')
# ['apple', 'banana', 'cherry']

# Menambah di posisi tertentu / Add at specific position
fruits.insert(1, 'apricot')
# ['apple', 'apricot', 'banana', 'cherry']

# Menambah multiple items / Add multiple items
fruits.extend(['date', 'elderberry'])
# ['apple', 'apricot', 'banana', 'cherry', 'date', 'elderberry']

# Menggunakan operator + / Using + operator
more_fruits = fruits + ['fig', 'grape']
```

### 4. Menghapus Elemen / Removing Elements

```python
fruits = ['apple', 'banana', 'cherry', 'banana', 'date']

# Hapus berdasarkan nilai / Remove by value (first occurrence)
fruits.remove('banana')
# ['apple', 'cherry', 'banana', 'date']

# Hapus berdasarkan indeks / Remove by index
deleted = fruits.pop(1)   # deleted = 'cherry'
last = fruits.pop()       # Hapus terakhir / Remove last

# Hapus dengan del / Delete with del
del fruits[0]

# Hapus beberapa elemen / Delete multiple elements
del fruits[1:3]

# Hapus semua / Clear all
fruits.clear()
```

### 5. Memodifikasi Elemen / Modifying Elements

```python
fruits = ['apple', 'banana', 'cherry']

# Ubah satu elemen / Change single element
fruits[1] = 'blueberry'
# ['apple', 'blueberry', 'cherry']

# Ubah beberapa elemen / Change multiple elements
fruits[0:2] = ['apricot', 'blackberry']
# ['apricot', 'blackberry', 'cherry']
```

### 6. Method Penting / Important Methods

```python
numbers = [3, 1, 4, 1, 5, 9, 2, 6]

# Mengurutkan / Sorting
numbers.sort()               # Ascending: [1, 1, 2, 3, 4, 5, 6, 9]
numbers.sort(reverse=True)   # Descending: [9, 6, 5, 4, 3, 2, 1, 1]
sorted_nums = sorted(numbers)  # Membuat list baru / Creates new list

# Membalik urutan / Reverse order
numbers.reverse()

# Menghitung kemunculan / Count occurrences
count = numbers.count(1)  # 2

# Mencari indeks / Find index
index = numbers.index(5)  # Indeks pertama dari 5

# Menyalin list / Copy list
copy = numbers.copy()
copy = numbers[:]

# Panjang list / Length
length = len(numbers)

# Min, Max, Sum
print(min(numbers))  # Nilai terkecil
print(max(numbers))  # Nilai terbesar
print(sum(numbers))  # Total
```

### 7. Iterasi / Iteration

```python
genz_slang = ['cap', 'bussin', 'slay', 'bestie']

# Iterasi sederhana / Simple iteration
for word in genz_slang:
    print(word)

# Iterasi dengan indeks / Iteration with index
for i in range(len(genz_slang)):
    print(f'{i}: {genz_slang[i]}')

# Menggunakan enumerate (recommended)
for index, word in enumerate(genz_slang):
    print(f'{index}: {word}')

# Iterasi dengan kondisi / Iteration with condition
for word in genz_slang:
    if len(word) > 3:
        print(word)
```

### 8. List Comprehension

```python
# Sintaks: [expression for item in iterable if condition]

# Kuadrat angka / Square numbers
squares = [x**2 for x in range(5)]
# [0, 1, 4, 9, 16]

# Dengan kondisi / With condition
even_squares = [x**2 for x in range(10) if x % 2 == 0]
# [0, 4, 16, 36, 64]

# Mengubah ke uppercase / Convert to uppercase
words = ['hello', 'world']
upper = [w.upper() for w in words]
# ['HELLO', 'WORLD']

# Nested list comprehension
matrix = [[i*j for j in range(3)] for i in range(3)]
# [[0, 0, 0], [0, 1, 2], [0, 2, 4]]
```

### 9. Nested List

```python
# List dalam list / List inside list
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Akses elemen nested / Access nested element
print(matrix[0][1])  # Output: 2 (baris 0, kolom 1)

# Iterasi nested list / Iterate nested list
for row in matrix:
    for item in row:
        print(item, end=' ')
    print()
```

---

## ✅ Best Practices

### 🇮🇩 Bahasa Indonesia

| #   | Praktik                           | Penjelasan                                                         |
| --- | --------------------------------- | ------------------------------------------------------------------ |
| 1   | Gunakan `enumerate()`             | Lebih Pythonic daripada `range(len())` untuk iterasi dengan indeks |
| 2   | Gunakan list comprehension        | Lebih ringkas dan efisien dari loop biasa                          |
| 3   | Hindari modifikasi saat iterasi   | Buat copy dulu jika perlu menghapus/menambah elemen                |
| 4   | Gunakan `in` untuk cek keberadaan | `if item in list:` lebih mudah dibaca                              |
| 5   | Pilih `append()` vs `extend()`    | `append()` untuk satu item, `extend()` untuk banyak                |
| 6   | Gunakan `sorted()` vs `.sort()`   | `sorted()` buat list baru, `.sort()` ubah yang ada                 |
| 7   | Hati-hati dengan referensi        | `b = a` hanya copy referensi, gunakan `.copy()` untuk copy nilai   |
| 8   | Gunakan unpacking                 | `first, *rest = list` untuk mengambil sebagian elemen              |

### 🇬🇧 English

| #   | Practice                        | Explanation                                                 |
| --- | ------------------------------- | ----------------------------------------------------------- |
| 1   | Use `enumerate()`               | More Pythonic than `range(len())` for indexed iteration     |
| 2   | Use list comprehension          | More concise and efficient than regular loops               |
| 3   | Avoid modifying while iterating | Create a copy first if you need to add/remove elements      |
| 4   | Use `in` to check existence     | `if item in list:` is more readable                         |
| 5   | Choose `append()` vs `extend()` | `append()` for single item, `extend()` for multiple         |
| 6   | Use `sorted()` vs `.sort()`     | `sorted()` creates new list, `.sort()` modifies in-place    |
| 7   | Be careful with references      | `b = a` only copies reference, use `.copy()` for value copy |
| 8   | Use unpacking                   | `first, *rest = list` to extract parts of the list          |

---

## 📝 Code Examples / Contoh Kode

### Contoh 1: Gen-Z Slang List

```python
genz_slang = ['cap', 'bussin', 'slay', 'bestie']
print(genz_slang)

# Akses individual
for i, word in enumerate(genz_slang):
    print(f'{i}: {word}')

# Menambah slang baru
genz_slang.append('no cap')
genz_slang.extend(['vibe', 'lit'])
```

### Contoh 2: Number Operations

```python
numbers = [3, 1, 4, 1, 5, 9, 2, 6]

# Statistik dasar / Basic statistics
print(f'Min: {min(numbers)}')
print(f'Max: {max(numbers)}')
print(f'Sum: {sum(numbers)}')
print(f'Avg: {sum(numbers) / len(numbers):.2f}')

# Filter dengan comprehension
positives = [n for n in numbers if n > 3]
print(f'Numbers > 3: {positives}')
```

### Contoh 3: Shopping Cart

```python
cart = []

# Menambah item
cart.append({'name': 'Laptop', 'price': 15000000})
cart.append({'name': 'Mouse', 'price': 250000})
cart.append({'name': 'Keyboard', 'price': 500000})

# Hitung total
total = sum(item['price'] for item in cart)
print(f'Total: Rp {total:,}')

# Hapus item
cart.remove({'name': 'Mouse', 'price': 250000})
```

---

## ⚠️ Common Mistakes / Kesalahan Umum

### ❌ Salah / Wrong

```python
# IndexError - indeks di luar jangkauan
my_list = [1, 2, 3]
print(my_list[5])  # IndexError!

# Memodifikasi list saat iterasi
for item in my_list:
    if item == 2:
        my_list.remove(item)  # Berbahaya / Dangerous!

# Copy hanya referensi
a = [1, 2, 3]
b = a
b.append(4)  # a juga berubah! / a also changes!
```

### ✅ Benar / Correct

```python
# Cek panjang dulu atau gunakan try-except
if len(my_list) > 5:
    print(my_list[5])

# Buat copy untuk iterasi yang dimodifikasi
for item in my_list.copy():
    if item == 2:
        my_list.remove(item)

# Copy nilai dengan benar
a = [1, 2, 3]
b = a.copy()  # atau b = a[:]
b.append(4)   # a tidak berubah / a unchanged
```

---

## 🔄 List vs Other Data Structures

| Fitur      | List               | Tuple          | Set          | Dict            |
| ---------- | ------------------ | -------------- | ------------ | --------------- |
| Mutable    | ✅                 | ❌             | ✅           | ✅              |
| Ordered    | ✅                 | ✅             | ❌           | ✅\*            |
| Indexed    | ✅                 | ✅             | ❌           | Key-based       |
| Duplicates | ✅                 | ✅             | ❌           | Keys ❌         |
| Use Case   | General collection | Immutable data | Unique items | Key-value pairs |

\*Dict ordered sejak Python 3.7+ / Dict ordered since Python 3.7+

---

## 📚 Referensi / References

- [Python Official Documentation - Lists](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists)
- [Real Python - Python Lists](https://realpython.com/python-lists-tuples/)
