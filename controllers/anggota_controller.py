
# PASHA AHMAD_F5212520082

import tkinter.messagebox as messagebox
from models.anggota_model import AnggotaModel
from views.anggota_view import AnggotaView


class AnggotaController:
    def __init__(self):
        # Inisialisasi Model dan View
        self.model = AnggotaModel()
        self.view = AnggotaView()

        # Menghubungkan tombol Simpan dengan Controller
        self.view.btn_simpan.configure(
            command=self.simpan_data
        )

        # Memuat data anggota saat aplikasi dibuka
        self.muat_data_tabel()

    def muat_data_tabel(self):
        # Mengosongkan tabel terlebih dahulu
        for item in self.view.tabel.get_children():
            self.view.tabel.delete(item)

        # Mengambil data anggota dari Model
        data_anggota = self.model.get_all_anggota()

        # Memasukkan data ke tabel
        for anggota in data_anggota:
            self.view.tabel.insert(
                "",
                "end",
                values=(
                    anggota["id_anggota"],
                    anggota["nama"],
                    anggota["alamat"]
                )
            )

    def simpan_data(self):
        # Mengambil data dari form
        nama = self.view.entry_nama.get().strip()
        alamat = self.view.entry_alamat.get().strip()

        # Validasi form kosong
        if not nama or not alamat:
            messagebox.showwarning(
                "Peringatan",
                "Nama dan alamat harus diisi!"
            )
            return

        # Menyimpan data melalui Model
        berhasil = self.model.create_anggota(
            nama, alamat
        )

        if berhasil:
            messagebox.showinfo(
                "Sukses",
                "Data anggota berhasil disimpan!"
            )

            # Membersihkan form
            self.bersihkan_form()

            # Memuat ulang tabel
            self.muat_data_tabel()

        else:
            messagebox.showerror(
                "Error",
                "Data anggota gagal disimpan."
            )

    def bersihkan_form(self):
        # Mengosongkan input
        self.view.entry_nama.delete(0, "end")
        self.view.entry_alamat.delete(0, "end")

    # Menjalankan aplikasi
    def run(self):
        self.view.mainloop()


if __name__ == "__main__":
    app = AnggotaController()
    app.run()
