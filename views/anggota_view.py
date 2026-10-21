import customtkinter as ctk
from tkinter import ttk

import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from models.anggota_model import AnggotaModel


class AnggotaView(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Data Anggota Perpustakaan")
        self.geometry("1000x600")

        # Membuat model anggota
        self.model = AnggotaModel()

        # Konfigurasi Grid Utama
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=2)
        self.grid_rowconfigure(0, weight=1)

        # ==========================================
        # FRAME KIRI: FORM DATA ANGGOTA
        # ==========================================
        self.frame_kiri = ctk.CTkFrame(self)
        self.frame_kiri.grid(
            row=0,
            column=0,
            padx=10,
            pady=10,
            sticky="nsew"
        )

        ctk.CTkLabel(
            self.frame_kiri,
            text="Form Data Anggota",
            font=("Arial", 18, "bold")
        ).pack(pady=30)

        # Label Nama
        ctk.CTkLabel(
            self.frame_kiri,
            text="Nama Anggota",
            font=("Arial", 14)
        ).pack(pady=10)

        # Input Nama
        self.entry_nama = ctk.CTkEntry(
            self.frame_kiri,
            placeholder_text="Masukkan Nama Anggota",
            height=35
        )
        self.entry_nama.pack(
            pady=5,
            padx=20,
            fill="x"
        )

        # Label Alamat
        ctk.CTkLabel(
            self.frame_kiri,
            text="Alamat",
            font=("Arial", 14)
        ).pack(pady=20)

        # Input Alamat
        self.entry_alamat = ctk.CTkEntry(
            self.frame_kiri,
            placeholder_text="Masukkan Alamat",
            height=35
        )
        self.entry_alamat.pack(
            pady=5,
            padx=20,
            fill="x"
        )

        # Tombol Simpan
        self.btn_simpan = ctk.CTkButton(
            self.frame_kiri,
            text="Simpan Data",
            fg_color="green",
            height=35,
            command=self.simpan_data
        )
        self.btn_simpan.pack(
            pady=30,
            padx=20,
            fill="x"
        )

        # ==========================================
        # FRAME KANAN: DAFTAR ANGGOTA
        # ==========================================
        self.frame_kanan = ctk.CTkFrame(self)
        self.frame_kanan.grid(
            row=0,
            column=1,
            padx=10,
            pady=10,
            sticky="nsew"
        )

        ctk.CTkLabel(
            self.frame_kanan,
            text="Daftar Anggota Perpustakaan",
            font=("Arial", 18, "bold")
        ).pack(pady=20)

        # Identitas Mahasiswa
        ctk.CTkLabel(
            self.frame_kanan,
            text="PASHA AHMAD | F5212520082",
            font=("Arial", 12, "bold")
        ).pack(pady=5)

        # ==========================================
        # TABEL ANGGOTA
        # ==========================================
        kolom = ("id_anggota", "nama", "alamat")

        self.tabel = ttk.Treeview(
            self.frame_kanan,
            columns=kolom,
            show="headings",
            height=18
        )

        # Header tabel
        self.tabel.heading(
            "id_anggota",
            text="ID Anggota"
        )

        self.tabel.heading(
            "nama",
            text="Nama Anggota"
        )

        self.tabel.heading(
            "alamat",
            text="Alamat"
        )

        # Lebar kolom
        self.tabel.column(
            "id_anggota",
            width=100,
            anchor="center"
        )

        self.tabel.column(
            "nama",
            width=200
        )

        self.tabel.column(
            "alamat",
            width=250
        )

        self.tabel.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=15
        )

        # Menampilkan data dari database
        self.tampilkan_data()

    # ==========================================
    # FUNGSI MENYIMPAN DATA
    # ==========================================
    def simpan_data(self):
        nama = self.entry_nama.get()
        alamat = self.entry_alamat.get()

        if nama and alamat:
            self.model.create_anggota(nama, alamat)

            self.entry_nama.delete(0, "end")
            self.entry_alamat.delete(0, "end")

            self.tampilkan_data()

    # ==========================================
    # FUNGSI MENAMPILKAN DATA
    # ==========================================
    def tampilkan_data(self):

        # Membersihkan isi tabel
        for item in self.tabel.get_children():
            self.tabel.delete(item)

        # Mengambil data dari database
        daftar_anggota = self.model.get_all_anggota()

        # Memasukkan data ke tabel
        for anggota in daftar_anggota:
            self.tabel.insert(
                "",
                "end",
                values=(
                    anggota["id_anggota"],
                    anggota["nama"],
                    anggota["alamat"]
                )
            )


# ==========================================
# BLOK EKSEKUSI
# ==========================================
if __name__ == "__main__":
    app = AnggotaView()
    app.mainloop()