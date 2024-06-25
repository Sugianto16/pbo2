from connection import create_connection
from interfaces.MahasiswaInterface import *
from interfaces.DashboardInterface import *
from interfaces.ProdiInterface import *
from interfaces.KelulusanInterface import *

class CoreModel(MahasiswaInterface, DashboardInterface, ProdiInterface, KelulusanInterface):
    def __init__(self):
        pass

    # ----------- mahasiswa --------------

    #table mahasiswa relasi tabel prodi
    def all_mahasiswa(self):
        connection = create_connection()
        cursor = connection.cursor()
        query = f"SELECT m.*, p.nama_prodi FROM {self.table_name} m JOIN prodi p ON m.id_prodi = p.id"
        cursor.execute(query)
        result = cursor.fetchall()
        cursor.close()
        connection.close()
        return result

    # mencari berdasarkan nim
    def find_by_nim(self, nim):
        connection = create_connection()
        cursor = connection.cursor()
        query = f"SELECT * FROM {self.table_name} WHERE nim = %s LIMIT 1"
        cursor.execute(query, (nim,))
        result = cursor.fetchone()
        cursor.close()
        connection.close()
        return result
    
    # menghitung jumlah baris mahasiswa
    def count_rows_mahasiswa(self):
        connection = create_connection()
        cursor = connection.cursor()

        query = f"SELECT COUNT(*) FROM {self.table_name}"
        cursor.execute(query)
        result = cursor.fetchone()

        cursor.close()
        connection.close()

        return result
    