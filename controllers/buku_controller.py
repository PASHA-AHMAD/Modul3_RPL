
# PASHA AHMAD_F5212520082
import tkinter.messagebox as messagebox
from models.buku_model import BukuModel
from views.buku_view import BukuView


class BukuController:
    def __init__(self, user_role="anggota"):
        self.user_role = user_role.lower()
        self.model = BukuModel()
        self.view = BukuView()

        # Menyimpan ID buku yang dipilih
        self.selected_id = None

        # Binding tombol
        self.view.btn_logout.configure(command=self.logout)
        self.view.btn_simpan.configure(command=self.simpan_data)
        self.view.btn_update.configure(command=self.update_data)
        self.view.btn_delete.configure(command=self.delete_data)

        # Binding pemilihan baris tabel
        self.view.tabel.bind("<<TreeviewSelect>>", self.pilih_buku)

        # Judul aplikasi
        self.view.title(
            f"Sistem Manajemen Perpustakaan - Mode: {self.user_role.upper()}"
        )

        # Otorisasi anggota
        if self.user_role != "admin":
            self.view.btn_simpan.configure(
                state="disabled",
                text="Akses Terkunci (Khusus Admin)"
            )
            self.view.btn_update.configure(
                state="disabled",
                text="Akses Terkunci (Khusus Admin)"
            )
            self.view.btn_delete.configure(
                state="disabled",
                text="Akses Terkunci (Khusus Admin)"
            )
            self.view.entry_judul.configure(state="disabled")
            self.view.entry_penulis.configure(state="disabled")
            self.view.entry_tahun.configure(state="disabled")

        self.muat_data_tabel()

    # MENAMPILKAN DATA BUKU
    def muat_data_tabel(self):
        for item in self.view.tabel.get_children():
            self.view.tabel.delete(item)

        data_buku = self.model.get_all_buku()

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

        self.selected_id = None

    # MENGAMBIL DATA DARI BARIS YANG DIPILIH
    def pilih_buku(self, event=None):
        selected = self.view.tabel.selection()

        if not selected:
            return

        item = self.view.tabel.item(selected[0])
        values = item["values"]

        if not values:
            return

        self.selected_id = values[0]

        if self.user_role == "admin":
            self.view.entry_judul.delete(0, "end")
            self.view.entry_penulis.delete(0, "end")
            self.view.entry_tahun.delete(0, "end")

            self.view.entry_judul.insert(0, values[1])
            self.view.entry_penulis.insert(0, values[2])
            self.view.entry_tahun.insert(0, values[3])

    # MENYIMPAN DATA BUKU
    def simpan_data(self):
        if self.user_role != "admin":
            messagebox.showerror(
                "Akses Ditolak",
                "Anda tidak memiliki izin untuk menambah data!"
            )
            return

        judul = self.view.entry_judul.get().strip()
        penulis = self.view.entry_penulis.get().strip()
        tahun = self.view.entry_tahun.get().strip()

        if not judul or not penulis or not tahun:
            messagebox.showwarning(
                "Peringatan",
                "Semua kolom form harus diisi!"
            )
            return

        if not tahun.isdigit():
            messagebox.showwarning(
                "Peringatan",
                "Tahun terbit harus berupa angka!"
            )
            return

        hasil = self.model.create_buku(judul, penulis, int(tahun))

        if hasil:
            messagebox.showinfo("Sukses", "Data buku berhasil disimpan!")
            self.kosongkan_form()
            self.muat_data_tabel()
        else:
            messagebox.showerror("Error", "Gagal menyimpan data!")

    # MEMPERBARUI DATA BUKU
    def update_data(self):
        if self.user_role != "admin":
            messagebox.showerror("Akses Ditolak", "Khusus Admin!")
            return

        if self.selected_id is None:
            messagebox.showwarning(
                "Peringatan",
                "Pilih buku dari tabel terlebih dahulu!"
            )
            return

        judul = self.view.entry_judul.get().strip()
        penulis = self.view.entry_penulis.get().strip()
        tahun = self.view.entry_tahun.get().strip()

        if not judul or not penulis or not tahun:
            messagebox.showwarning(
                "Peringatan",
                "Semua kolom harus diisi!"
            )
            return

        if not tahun.isdigit():
            messagebox.showwarning(
                "Peringatan",
                "Tahun terbit harus berupa angka!"
            )
            return

        hasil = self.model.update_buku(
            self.selected_id,
            judul,
            penulis,
            int(tahun)
        )

        if hasil:
            messagebox.showinfo(
                "Sukses",
                "Data buku berhasil diperbarui!"
            )
            self.kosongkan_form()
            self.muat_data_tabel()
        else:
            messagebox.showerror(
                "Gagal",
                "Data buku tidak ditemukan atau gagal diperbarui!"
            )

    # MENGHAPUS DATA BUKU
    def delete_data(self):
        if self.user_role != "admin":
            messagebox.showerror("Akses Ditolak", "Khusus Admin!")
            return

        if self.selected_id is None:
            messagebox.showwarning(
                "Peringatan",
                "Pilih buku dari tabel terlebih dahulu!"
            )
            return

        konfirmasi = messagebox.askyesno(
            "Konfirmasi",
            "Apakah Anda yakin ingin menghapus buku ini?"
        )

        if not konfirmasi:
            return

        hasil = self.model.delete_buku(self.selected_id)

        if hasil:
            messagebox.showinfo(
                "Sukses",
                "Data buku berhasil dihapus!"
            )
            self.kosongkan_form()
            self.muat_data_tabel()
        else:
            messagebox.showerror(
                "Gagal",
                "Data buku tidak ditemukan atau gagal dihapus!"
            )

    # MENGOSONGKAN FORM
    def kosongkan_form(self):
        if self.user_role == "admin":
            self.view.entry_judul.delete(0, "end")
            self.view.entry_penulis.delete(0, "end")
            self.view.entry_tahun.delete(0, "end")

        self.selected_id = None

        for item in self.view.tabel.selection():
            self.view.tabel.selection_remove(item)

    # LOGOUT
    def logout(self):
        self.view.destroy()

        from controllers.auth_controller import AuthController
        app_login = AuthController()
        app_login.run()

    # MENJALANKAN APLIKASI
    def run(self):
        self.view.mainloop()
