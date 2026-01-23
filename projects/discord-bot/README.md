# Discord Meme Bot

Bot Discord sederhana yang dapat merespons pesan dan mengirim meme secara acak.

## Fitur

- **$hello** - Bot akan membalas dengan "Hello World!"
- **$meme** - Bot akan mengirim meme acak dari internet

## Prasyarat

Sebelum menjalankan bot ini, pastikan Anda sudah memiliki:

1. **Python 3.8+** terinstall di komputer
2. **Akun Discord** untuk membuat bot
3. **Bot Token** dari Discord Developer Portal

## Instalasi

### 1. Install Dependencies

Buka terminal/command prompt dan jalankan perintah berikut:

```bash
pip install discord.py requests
```

### 2. Dapatkan Bot Token

1. Buka [Discord Developer Portal](https://discord.com/developers/applications)
2. Klik **"New Application"** dan beri nama aplikasi
3. Pergi ke menu **"Bot"** di sidebar kiri
4. Klik **"Add Bot"**
5. Klik **"Reset Token"** untuk mendapatkan token baru
6. **Salin token** tersebut (simpan dengan aman, jangan bagikan ke siapapun!)

### 3. Konfigurasi Bot Token

Buka file `bot.py` dan ganti `'YOUR_BOT_TOKEN'` dengan token bot Anda:

```python
client.run('YOUR_BOT_TOKEN')  # Ganti dengan token asli
```

Contoh:

```python
client.run('MTIzNDU2Nzg5MDEyMzQ1Njc4OQ.ABC123.xyz789...')
```

### 4. Aktifkan Message Content Intent

1. Di Discord Developer Portal, pergi ke aplikasi bot Anda
2. Buka menu **"Bot"**
3. Scroll ke bawah ke bagian **"Privileged Gateway Intents"**
4. Aktifkan **"Message Content Intent"**
5. Simpan perubahan

### 5. Undang Bot ke Server Discord

1. Di Discord Developer Portal, pergi ke menu **"OAuth2"** > **"URL Generator"**
2. Di bagian **"Scopes"**, centang:
   - `bot`
3. Di bagian **"Bot Permissions"**, centang:
   - `Send Messages`
   - `Read Message History`
4. Salin URL yang dihasilkan dan buka di browser
5. Pilih server Discord tujuan dan klik **"Authorize"**

## Cara Menjalankan

1. Buka terminal/command prompt
2. Navigasi ke folder project:
   ```bash
   cd path/to/discord-bot
   ```
3. Jalankan bot:
   ```bash
   python bot.py
   ```
4. Jika berhasil, akan muncul pesan:
   ```
   Logged on as NamaBot#1234
   ```

## Penggunaan

Setelah bot berjalan dan terhubung ke server Discord:

| Perintah | Deskripsi                          |
| -------- | ---------------------------------- |
| `$hello` | Bot membalas dengan "Hello World!" |
| `$meme`  | Bot mengirim meme acak             |

## Troubleshooting

### Error: "ModuleNotFoundError"

Pastikan sudah menginstall dependencies:

```bash
pip install discord.py requests
```

### Error: "Improper token has been passed"

Pastikan token bot sudah benar dan tidak ada spasi tambahan.

### Bot tidak merespons perintah

1. Pastikan **Message Content Intent** sudah diaktifkan
2. Pastikan bot memiliki permission untuk membaca dan mengirim pesan di channel

## Catatan Keamanan

> ⚠️ **PENTING**: Jangan pernah membagikan bot token Anda ke siapapun atau meng-upload ke repository publik. Jika token bocor, segera reset token di Discord Developer Portal.
