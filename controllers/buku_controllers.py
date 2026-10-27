# PASHA AHMAD_F5212520082
import tkinter.messagebox as messagebox
from models.buku_model import BukuModel
from views.buku_view import BukuView


class BukuController:
    def __init__(self):
        # Inisialisasi Model dan View
        self.model = BukuModel()
        self.view = BukuView()

        # Menyimpan ID buku yang dipilih
        self.id_buku_dipilih = None

        # Binding tombol dengan fungsi Controller
        self.view.btn_simpan.configure(
            command=self.simpan_data
        )
        self.view.btn_update.configure(
            command=self.perbarui_data
        )
        self.view.btn_delete.configure(
            command=self.hapus_data
        )

        # Binding pemilihan baris tabel
        self.view.tabel.bind(
            "<<TreeviewSelect>>",
            self.pilih_data
        )

        # Memuat data saat aplikasi dibuka
        self.muat_data_tabel()

    def muat_data_tabel(self):
        # Mengosongkan tabel
        for item in self.view.tabel.get_children():
            self.view.tabel.delete(item)

        # Mengambil data dari Model
        data_buku = self.model.get_all_buku()

        # Menampilkan data ke tabel
        for buku in data_buku:
            self.view.tabel.insert(
                "",
                "end",
                values=(
                    buku["id_buku"],
                    buku["judul"],
                    buku["penulis"],
                    buku["tahun_terbit"]
                )
            )

    def pilih_data(self, event=None):
        # Mengambil baris yang dipilih
        pilihan = self.view.tabel.selection()

        if not pilihan:
            return

        data = self.view.tabel.item(
            pilihan[0], "values"
        )

        # Mengambil ID buku dari kolom pertama
        self.id_buku_dipilih = int(data[0])

        # Memasukkan data ke form
        self.view.entry_judul.delete(0, "end")
        self.view.entry_judul.insert(0, data[1])

        self.view.entry_penulis.delete(0, "end")
        self.view.entry_penulis.insert(0, data[2])

        self.view.entry_tahun.delete(0, "end")
        self.view.entry_tahun.insert(0, data[3])

    def simpan_data(self):
        # Mengambil input dari form
        judul = self.view.entry_judul.get().strip()
        penulis = self.view.entry_penulis.get().strip()
        tahun = self.view.entry_tahun.get().strip()

        # Validasi form
        if not judul or not penulis or not tahun:
            messagebox.showwarning(
                "Peringatan",
                "Semua kolom form harus diisi!"
            )
            return

        try:
            tahun = int(tahun)
        except ValueError:
            messagebox.showwarning(
                "Peringatan",
                "Tahun terbit harus berupa angka!"
            )
            return

        # Menyimpan data melalui Model
        berhasil = self.model.create_buku(
            judul, penulis, tahun
        )

        if berhasil is not None:
            messagebox.showinfo(
                "Sukses",
                "Data buku berhasil disimpan!"
            )
            self.bersihkan_form()
            self.muat_data_tabel()
        else:
            messagebox.showerror(
                "Error",
                "Data buku gagal disimpan."
            )

    def perbarui_data(self):
        # Memastikan baris sudah dipilih
        if self.id_buku_dipilih is None:
            messagebox.showwarning(
                "Peringatan",
                "Pilih buku yang ingin diperbarui!"
            )
            return

        # Mengambil data terbaru dari form
        judul = self.view.entry_judul.get().strip()
        penulis = self.view.entry_penulis.get().strip()
        tahun = self.view.entry_tahun.get().strip()

        if not judul or not penulis or not tahun:
            messagebox.showwarning(
                "Peringatan",
                "Semua kolom form harus diisi!"
            )
            return

        try:
            tahun = int(tahun)
        except ValueError:
            messagebox.showwarning(
                "Peringatan",
                "Tahun terbit harus berupa angka!"
            )
            return

        # Konfirmasi pembaruan
        konfirmasi = messagebox.askyesno(
            "Konfirmasi",
            "Apakah data buku ingin diperbarui?"
        )

        if not konfirmasi:
            return

        # Memanggil fungsi UPDATE pada Model
        berhasil = self.model.update_buku(
            self.id_buku_dipilih,
            judul,
            penulis,
            tahun
        )

        if berhasil:
            messagebox.showinfo(
                "Sukses",
                "Data buku berhasil diperbarui!"
            )
            self.bersihkan_form()
            self.muat_data_tabel()
        else:
            messagebox.showerror(
                "Error",
                "Data buku gagal diperbarui."
            )

    def hapus_data(self):
        # Memastikan baris sudah dipilih
        if self.id_buku_dipilih is None:
            messagebox.showwarning(
                "Peringatan",
                "Pilih buku yang ingin dihapus!"
            )
            return

        # Konfirmasi penghapusan
        konfirmasi = messagebox.askyesno(
            "Konfirmasi",
            "Apakah data buku ingin dihapus?"
        )

        if not konfirmasi:
            return

        # Memanggil fungsi DELETE pada Model
        berhasil = self.model.delete_buku(
            self.id_buku_dipilih
        )

        if berhasil:
            messagebox.showinfo(
                "Sukses",
                "Data buku berhasil dihapus!"
            )
            self.bersihkan_form()
            self.muat_data_tabel()
        else:
            messagebox.showerror(
                "Error",
                "Data buku gagal dihapus."
            )

    def bersihkan_form(self):
        # Membersihkan semua input
        self.view.entry_judul.delete(0, "end")
        self.view.entry_penulis.delete(0, "end")
        self.view.entry_tahun.delete(0, "end")

        # Menghapus ID buku terpilih
        self.id_buku_dipilih = None

        # Menghapus seleksi tabel
        self.view.tabel.selection_remove(
            self.view.tabel.selection()
        )

    # Menjalankan aplikasi
    def run(self):
        self.view.mainloop()


if __name__ == "__main__":
    app = BukuController()
    app.run()
