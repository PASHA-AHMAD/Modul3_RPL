# PASHA AHMAD_F5212520082
from config.database import Database


class BukuModel:
    def __init__(self):
        self.db = Database()
        self.conn = self.db.get_connection()
        self.table_name = "buku"

    # READ
    def get_all_buku(self):
        if self.conn:
            cursor = self.conn.cursor(dictionary=True)

            query = f"SELECT * FROM {self.table_name}"
            cursor.execute(query)

            result = cursor.fetchall()

            cursor.close()
            return result

        return []

    # CREATE
    def create_buku(self, judul, penulis, tahun_terbit):
        if self.conn:
            cursor = self.conn.cursor()

            query = f"""
                INSERT INTO {self.table_name}
                (judul, penulis, tahun_terbit)
                VALUES (%s, %s, %s)
            """

            val = (judul, penulis, tahun_terbit)

            cursor.execute(query, val)
            self.conn.commit()

            # Mengambil ID buku yang baru dibuat oleh MySQL
            id_buku = cursor.lastrowid

            cursor.close()

            return id_buku

        return None

    # UPDATE
    def update_buku(self, id_buku, judul, penulis, tahun_terbit):
        if self.conn:
            cursor = self.conn.cursor()

            query = f"""
                UPDATE {self.table_name}
                SET judul = %s,
                    penulis = %s,
                    tahun_terbit = %s
                WHERE id_buku = %s
            """

            val = (judul, penulis, tahun_terbit, id_buku)

            cursor.execute(query, val)
            self.conn.commit()

            cursor.close()
            return True

        return False

    # DELETE
    def delete_buku(self, id_buku):
        if self.conn:
            cursor = self.conn.cursor()

            query = f"""
                DELETE FROM {self.table_name}
                WHERE id_buku = %s
            """

            val = (id_buku,)

            cursor.execute(query, val)
            self.conn.commit()

            cursor.close()
            return True

        return False