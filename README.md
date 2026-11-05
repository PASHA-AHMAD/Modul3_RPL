# Aplikasi Perpustakaan

![CI Pipeline](../../actions/workflows/ci_pipeline.yml/badge.svg)

## Deskripsi Singkat

Aplikasi Perpustakaan adalah aplikasi desktop berbasis Python untuk mengelola data perpustakaan, seperti data buku dan transaksi, dengan antarmuka grafis. Aplikasi dibangun dengan pola arsitektur **MVC (Model-View-Controller)** dan menggunakan **MySQL** sebagai basis data.

Fitur utama:

- Halaman **Login** (Username dan Password) untuk membatasi akses hanya bagi pengguna yang memiliki akun.
- Pengelolaan data perpustakaan (tambah, lihat, ubah, hapus).
- Pengujian otomatis dengan **pytest** dan pemeriksaan kualitas kode dengan **flake8** melalui **GitHub Actions**.

## Struktur Direktori (MVC)

```
Modul3/
├── .github/
│   └── workflows/
│       └── ci_pipeline.yml      # Pipeline CI (flake8 + pytest)
├── config/                      # Konfigurasi aplikasi & koneksi database
├── controllers/                 # Controller: penghubung View dan Model
├── models/                      # Model: logika data & akses database MySQL
│   ├── anggota_model.py
│   ├── buku_model.py
│   └── user_model.py
├── views/                       # View: tampilan antarmuka (GUI)
├── tests/                       # Unit test (pytest)
├── build/                       # Berkas sementara hasil build PyInstaller
├── dist/                        # Hasil build (AplikasiPerpustakaan.exe)
├── main.py                      # Titik masuk aplikasi
├── test_anggota.py              # Pengujian model anggota
├── test_model.py                # Pengujian model
├── requirements.txt             # Daftar dependensi Python
├── .gitignore
└── README.md
```

| Lapisan | Peran |
|---|---|
| **Model** | Mengelola data dan berkomunikasi dengan database MySQL |
| **View** | Menampilkan antarmuka kepada pengguna |
| **Controller** | Menerima aksi dari View, memprosesnya lewat Model, lalu memperbarui View |

## Panduan Instalasi

### 1. Prasyarat

- Python 3.10 atau lebih baru
- MySQL Server 8.x (atau XAMPP/Laragon dengan MySQL aktif)
- Git

### 2. Clone Repositori

```bash
git clone https://github.com/PASHA-AHMAD/Modul3_RPL.git
cd Modul3_RPL
```

### 3. Buat Virtual Environment dan Instal Dependensi

```bash
python -m venv env
env\Scripts\activate
pip install -r requirements.txt
```

## Konfigurasi Database MySQL

Aplikasi menggunakan database MySQL bernama **`perpustakaan`** yang berisi empat tabel:

| Tabel | Fungsi |
|---|---|
| `users` | Data akun pengguna untuk login |
| `anggota` | Data anggota perpustakaan |
| `buku` | Data koleksi buku |
| `peminjaman` | Data transaksi peminjaman buku |

### Langkah Konfigurasi

1. Pastikan layanan MySQL (Laragon/XAMPP/MySQL Server) sudah berjalan.
2. Buat database baru bernama `perpustakaan`:

   ```sql
   CREATE DATABASE perpustakaan;
   USE perpustakaan;
   ```

3. Buat tabel `users`, `anggota`, `buku`, dan `peminjaman` di dalam database tersebut. Nama tabel dan kolom harus sesuai dengan query pada file di folder `models/` (`user_model.py`, `anggota_model.py`, `buku_model.py`).
4. Tambahkan minimal satu akun pada tabel `users` agar dapat digunakan untuk login.
5. Periksa bahwa keempat tabel sudah terbentuk:

   ```sql
   SHOW TABLES;
   ```

6. Sesuaikan koneksi database pada file `config/database.py` agar cocok dengan MySQL di komputer Anda:

   ```python
   host = "localhost"
   user = "root"
   password = ""            # isi sesuai password MySQL Anda
   database = "perpustakaan"
   ```

## Cara Menjalankan Aplikasi

### Dari Source Code

Aktifkan virtual environment, lalu jalankan:

```bash
python main.py
```

Halaman Login akan tampil. Masukkan **Username** dan **Password** yang terdaftar, lalu klik **Masuk**.

### Dari File Executable

Unduh `AplikasiPerpustakaan.exe` pada halaman **Releases** repositori ini, lalu jalankan dengan klik dua kali. Pastikan MySQL sudah aktif dan database sudah dikonfigurasi.

## Menjalankan Pengujian dan Linter

```bash
flake8 models/ controllers/ --count --select=E9,F63,F7,F82 --show-source --statistics
python -m pytest -v
```

Kedua perintah ini juga dijalankan otomatis oleh GitHub Actions setiap kali ada push ke branch `main`.
