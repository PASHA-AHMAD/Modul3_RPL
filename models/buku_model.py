
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
            try:
                query = f"SELECT * FROM {self.table_name}"
                cursor.execute(query)
                return cursor.fetchall()
            finally:
                cursor.close()

        return []

    # CREATE
    def create_buku(self, judul, penulis, tahun_terbit):
        if self.conn:
            cursor = self.conn.cursor()
            try:
                query = f"""
                    INSERT INTO {self.table_name}
                    (judul, penulis, tahun_terbit)
                    VALUES (%s, %s, %s)
                """

                cursor.execute(query, (judul, penulis, tahun_terbit))
                self.conn.commit()

                return cursor.lastrowid

            except Exception:
                self.conn.rollback()
                raise
            finally:
                cursor.close()

        return None

    # UPDATE
    def update_buku(self, id_buku, judul, penulis, tahun_terbit):
        if self.conn:
            cursor = self.conn.cursor()
            try:
                query = f"""
                    UPDATE {self.table_name}
                    SET judul = %s,
                        penulis = %s,
                        tahun_terbit = %s
                    WHERE id_buku = %s
                """

                cursor.execute(
                    query,
                    (judul, penulis, tahun_terbit, id_buku)
                )

                jumlah_data = cursor.rowcount
                self.conn.commit()

                return jumlah_data > 0

            except Exception:
                self.conn.rollback()
                raise
            finally:
                cursor.close()

        return False

    # DELETE
    def delete_buku(self, id_buku):
        if self.conn:
            cursor = self.conn.cursor()
            try:
                query = f"""
                    DELETE FROM {self.table_name}
                    WHERE id_buku = %s
                """

                cursor.execute(query, (id_buku,))

                jumlah_data = cursor.rowcount
                self.conn.commit()

                return jumlah_data > 0

            except Exception:
                self.conn.rollback()
                raise
            finally:
                cursor.close()

        return False
