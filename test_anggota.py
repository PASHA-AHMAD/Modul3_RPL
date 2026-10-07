#PASHA AHMAD_F5212520082
from models.anggota_model import AnggotaModel


model = AnggotaModel()

# 1. Menguji fungsi Create
print("=== Menambahkan Data Anggota ===")

model.create_anggota(
    "Pasha Ahmad",
    "Palu"
)

print("Data anggota berhasil disimpan ke MySQL!")


# 2. Menguji fungsi Read
print("\n=== Daftar Anggota ===")

daftar_anggota = model.get_all_anggota()

for anggota in daftar_anggota:
    print(f"[{anggota['id_anggota']}] {anggota['nama']} - {anggota['alamat']}")