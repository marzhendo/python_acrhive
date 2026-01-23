# Animated GIF Creator

Program Python sederhana untuk membuat animasi GIF dari kumpulan gambar.

## Persyaratan

- Python 3.x
- Library `imageio`

### Instalasi Library

```bash
pip install imageio
```

## Cara Pemakaian

### 1. Siapkan Gambar

Tempatkan file gambar (JPEG/PNG) yang ingin dijadikan GIF di folder yang sama dengan `gif.py`.

### 2. Edit Daftar Gambar

Buka file `gif.py` dan ubah list `filenames` sesuai nama file gambar Anda:

```python
filenames = ['pic-1.jpeg', 'pic-3.jpeg']  # Ganti dengan nama file gambar Anda
```

### 3. Konfigurasi Output

Sesuaikan parameter pada baris `iio.imwrite()`:

```python
iio.imwrite('NamaOutput.gif', images, duration=500, loop=0)
```

| Parameter          | Keterangan                                            |
| ------------------ | ----------------------------------------------------- |
| `'NamaOutput.gif'` | Nama file GIF hasil output                            |
| `duration`         | Durasi setiap frame dalam milidetik (500 = 0.5 detik) |
| `loop`             | Jumlah pengulangan (0 = loop tak terbatas)            |

### 4. Jalankan Program

```bash
python gif.py
```

## Contoh Penggunaan

Jika Anda memiliki gambar `foto1.png`, `foto2.png`, dan `foto3.png`:

```python
import imageio.v3 as iio

filenames = ['foto1.png', 'foto2.png', 'foto3.png']
images = []
for filename in filenames:
    images.append(iio.imread(filename))

iio.imwrite('hasil_animasi.gif', images, duration=1000, loop=0)
```

## Struktur Folder

```
animated_gif/
├── gif.py           # Script utama
├── README.md        # Dokumentasi ini
├── pic-1.jpeg       # Gambar input
├── pic-2.jpeg       # Gambar input
├── pic-3.jpeg       # Gambar input
└── *.gif            # File GIF hasil output
```

## Tips

- Gunakan gambar dengan ukuran yang sama untuk hasil terbaik
- Semakin kecil nilai `duration`, semakin cepat animasinya
- Format gambar yang didukung: JPEG, PNG, BMP, dll.
