# PASHA AHMAD_F5212520082
from models.buku_model import BukuModel


model = BukuModel()


# 1. Menguji fungsi Create (menambah buku baru)
print("Menambahkan data buku...")

id_buku = model.create_buku(
    "Pemrograman Python MVC",
    "Guido van Rossum",
    2023
)

print("Data berhasil disimpan ke MySQL!")
print(f"ID buku yang dibuat: {id_buku}\n")


# 2. Menguji fungsi Read (menampilkan data)
print("=== Daftar Buku ===")

daftar_buku = model.get_all_buku()

for buku in daftar_buku:
    print(
        f"[{buku['id_buku']}] "
        f"{buku['judul']} - "
        f"{buku['penulis']} "
        f"({buku['tahun_terbit']})"
    )


# 3. Menguji fungsi Update
print("\n=== Mengubah Data Buku ===")

model.update_buku(
    id_buku,
    "Pemrograman Python MVC",
    "Guido van Rossum",
    2024
)

print("Data buku berhasil diubah!")


# 4. Menampilkan hasil setelah Update
print("\n=== Data Setelah Update ===")

daftar_buku = model.get_all_buku()

for buku in daftar_buku:
    print(
        f"[{buku['id_buku']}] "
        f"{buku['judul']} - "
        f"{buku['penulis']} "
        f"({buku['tahun_terbit']})"
    )


# 5. Menguji fungsi Delete
print("\n=== Menghapus Data Buku ===")

model.delete_buku(id_buku)

print("Data buku berhasil dihapus!")


# 6. Menampilkan hasil setelah Delete
print("\n=== Data Setelah Delete ===")

daftar_buku = model.get_all_buku()

for buku in daftar_buku:
    print(
        f"[{buku['id_buku']}] "
        f"{buku['judul']} - "
        f"{buku['penulis']} "
        f"({buku['tahun_terbit']})"
    )