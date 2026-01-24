# Python Dictionaries / Kamus Python

---

## 📖 Informasi / Information

### 🇮🇩 Bahasa Indonesia

**Dictionary** adalah struktur data bawaan Python yang menyimpan pasangan **key-value** (kunci-nilai). Dictionary bersifat:

- **Mutable**: Dapat diubah setelah dibuat
- **Unordered** (Python < 3.7) / **Ordered** (Python 3.7+): Menjaga urutan penyisipan
- **Key Unik**: Setiap key harus unik, nilai dapat duplikat
- **Key Immutable**: Key harus bertipe data yang tidak dapat diubah (string, number, tuple)

**Sintaks Dasar:**

```python
nama_dict = {
    'key1': 'value1',
    'key2': 'value2'
}
```

### 🇬🇧 English

**Dictionary** is a built-in Python data structure that stores **key-value** pairs. Dictionaries are:

- **Mutable**: Can be modified after creation
- **Unordered** (Python < 3.7) / **Ordered** (Python 3.7+): Maintains insertion order
- **Unique Keys**: Each key must be unique, values can be duplicated
- **Immutable Keys**: Keys must be immutable types (string, number, tuple)

**Basic Syntax:**

```python
dict_name = {
    'key1': 'value1',
    'key2': 'value2'
}
```

---

## 🚀 Cara Penggunaan / Usage

### 1. Membuat Dictionary / Creating a Dictionary

```python
# Empty dictionary / Dictionary kosong
empty_dict = {}
empty_dict = dict()

# Dictionary dengan nilai / Dictionary with values
student = {
    'name': 'John Doe',
    'age': 20,
    'major': 'Computer Science',
    'gpa': 3.8
}

# Dari list of tuples / From list of tuples
pairs = [('a', 1), ('b', 2)]
dict_from_pairs = dict(pairs)  # {'a': 1, 'b': 2}
```

### 2. Mengakses Nilai / Accessing Values

```python
student = {'name': 'John', 'age': 20}

# Menggunakan bracket notation / Using bracket notation
print(student['name'])  # Output: John

# Menggunakan .get() (lebih aman / safer)
print(student.get('name'))       # Output: John
print(student.get('email'))      # Output: None (tidak error / no error)
print(student.get('email', 'N/A'))  # Output: N/A (nilai default / default value)
```

### 3. Menambah & Mengubah Nilai / Adding & Modifying Values

```python
student = {'name': 'John', 'age': 20}

# Menambah key baru / Adding new key
student['email'] = 'john@mail.com'

# Mengubah nilai / Modifying value
student['age'] = 21

# Menggunakan .update() untuk banyak nilai / Using .update() for multiple values
student.update({'gpa': 3.9, 'year': 2024})
```

### 4. Menghapus Item / Deleting Items

```python
student = {'name': 'John', 'age': 20, 'major': 'CS'}

# Menggunakan del / Using del
del student['age']

# Menggunakan .pop() - mengembalikan nilai / returns the value
major = student.pop('major')  # major = 'CS'

# Menggunakan .pop() dengan default
email = student.pop('email', 'not found')

# Menghapus item terakhir / Remove last item
last_item = student.popitem()

# Menghapus semua item / Clear all items
student.clear()
```

### 5. Method Penting / Important Methods

```python
laptop = {
    'brand': 'Asus',
    'price': 4000000,
    'color': 'black'
}

# Mendapatkan semua keys / Get all keys
print(laptop.keys())    # dict_keys(['brand', 'price', 'color'])

# Mendapatkan semua values / Get all values
print(laptop.values())  # dict_values(['Asus', 4000000, 'black'])

# Mendapatkan semua pasangan key-value / Get all key-value pairs
print(laptop.items())   # dict_items([('brand', 'Asus'), ('price', 4000000), ...])

# Mengecek keberadaan key / Check if key exists
print('brand' in laptop)  # True
print('ram' in laptop)    # False

# Mendapatkan jumlah item / Get number of items
print(len(laptop))  # 3
```

### 6. Iterasi / Iteration

```python
laptop = {'brand': 'Asus', 'price': 4000000}

# Iterasi keys
for key in laptop:
    print(key)

# Iterasi values
for value in laptop.values():
    print(value)

# Iterasi key-value pairs
for key, value in laptop.items():
    print(f'{key}: {value}')
```

### 7. Dictionary Comprehension

```python
# Membuat dictionary dari range / Create dictionary from range
squares = {x: x**2 for x in range(5)}
# Output: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# Dengan kondisi / With condition
even_squares = {x: x**2 for x in range(10) if x % 2 == 0}
# Output: {0: 0, 2: 4, 4: 16, 6: 36, 8: 64}
```

### 8. Nested Dictionary

```python
# Dictionary dalam dictionary / Dictionary inside dictionary
students = {
    'student1': {
        'name': 'John',
        'age': 20
    },
    'student2': {
        'name': 'Jane',
        'age': 22
    }
}

# Akses nested value
print(students['student1']['name'])  # Output: John
```

---

## ✅ Best Practices

### 🇮🇩 Bahasa Indonesia

| #   | Praktik                           | Penjelasan                                           |
| --- | --------------------------------- | ---------------------------------------------------- |
| 1   | Gunakan `.get()` untuk akses      | Menghindari `KeyError` jika key tidak ada            |
| 2   | Gunakan key yang deskriptif       | Contoh: `'user_name'` bukan `'un'`                   |
| 3   | Konsisten dalam penamaan key      | Gunakan `snake_case` atau `camelCase`, jangan campur |
| 4   | Gunakan `in` untuk cek keberadaan | `if 'key' in dict:` lebih Pythonic                   |
| 5   | Gunakan dictionary comprehension  | Lebih ringkas dan efisien dari loop biasa            |
| 6   | Hindari key yang mutable          | List tidak bisa jadi key, gunakan tuple              |
| 7   | Gunakan `.setdefault()`           | Atur nilai default saat key tidak ada                |
| 8   | Pertimbangkan `defaultdict`       | Untuk dictionary dengan nilai default otomatis       |

### 🇬🇧 English

| #   | Practice                      | Explanation                                    |
| --- | ----------------------------- | ---------------------------------------------- |
| 1   | Use `.get()` for access       | Avoids `KeyError` when key doesn't exist       |
| 2   | Use descriptive keys          | Example: `'user_name'` not `'un'`              |
| 3   | Be consistent with key naming | Use `snake_case` or `camelCase`, don't mix     |
| 4   | Use `in` to check existence   | `if 'key' in dict:` is more Pythonic           |
| 5   | Use dictionary comprehension  | More concise and efficient than regular loops  |
| 6   | Avoid mutable keys            | Lists can't be keys, use tuples instead        |
| 7   | Use `.setdefault()`           | Set default value when key doesn't exist       |
| 8   | Consider `defaultdict`        | For dictionaries with automatic default values |

---

## 📝 Code Examples / Contoh Kode

### Contoh 1: Student Info

```python
student_info = {
    'name': 'John Doe',
    'age': 20,
    'major': 'Computer Science',
    'gpa': 3.8,
    'is_active': True
}

# Akses dan modifikasi
print(student_info['name'])
student_info['age'] = 21

# Menggunakan methods
print('Keys:', student_info.keys())
print('Values:', student_info.values())
print('Items:', student_info.items())
```

### Contoh 2: Laptop Specs

```python
laptop = {
    'brand': 'Asus',
    'price': 4000000,
    'processor': 'i7',
    'ram': '16GB',
    'storage': '512GB'
}

# Akses aman dengan .get()
gpu = laptop.get('gpu', 'Integrated')
print(f'GPU: {gpu}')  # Output: GPU: Integrated
```

### Contoh 3: Art Collection

```python
artworks = {
    'mona_lisa': {
        'artist': 'Leonardo da Vinci',
        'period': 'Renaissance',
        'year': 1503
    },
    'starry_night': {
        'artist': 'Vincent van Gogh',
        'period': 'Post-Impressionism',
        'year': 1889
    }
}

# Iterasi nested dictionary
for name, details in artworks.items():
    print(f"{name}: {details['artist']} ({details['year']})")
```

---

## ⚠️ Common Mistakes / Kesalahan Umum

### ❌ Salah / Wrong

```python
# KeyError jika key tidak ada
value = my_dict['nonexistent_key']

# Menggunakan list sebagai key
invalid = {[1, 2]: 'value'}  # TypeError!

# Memodifikasi dict saat iterasi
for key in my_dict:
    del my_dict[key]  # RuntimeError!
```

### ✅ Benar / Correct

```python
# Gunakan .get() untuk akses aman
value = my_dict.get('nonexistent_key', 'default')

# Gunakan tuple sebagai key
valid = {(1, 2): 'value'}

# Buat copy untuk iterasi yang dimodifikasi
for key in list(my_dict.keys()):
    del my_dict[key]
```

---

## 📚 Referensi / References

- [Python Official Documentation - Dictionaries](https://docs.python.org/3/tutorial/datastructures.html#dictionaries)
- [Real Python - Dictionaries](https://realpython.com/python-dicts/)
