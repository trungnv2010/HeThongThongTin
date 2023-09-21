import mysql.connector
class Database:
    def __init__(self, host, user, password, database=None):
        self.connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        self.cursor = self.connection.cursor()

    def execute_query(self, query, params=None):
        if params:
            self.cursor.execute(query, params)
        else:
            self.cursor.execute(query)
        self.connection.commit()

    def fetch_query(self, query, params=None):
        if params:
            self.cursor.execute(query, params)
        else:
            self.cursor.execute(query)
        return self.cursor.fetchall()

    def close(self):
        self.cursor.close()
        self.connection.close()

    def create_database(self, db_name):
        self.cursor.execute(f"CREATE DATABASE IF NOT EXISTS {db_name}")
        self.cursor.execute(f"USE {db_name}")
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS SinhVien (
            ma_sv VARCHAR(255) PRIMARY KEY,
            ho_ten VARCHAR(255),
            dia_chi VARCHAR(255),
            ngay_sinh VARCHAR(255),
            khoa_hoc INT
        )
        """)
        
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS MonHoc (
            ma_mon_hoc VARCHAR(255) PRIMARY KEY,
            ten_mon_hoc VARCHAR(255),
            so_tin_chi INT,
            he_so FLOAT
        )
        """)
        
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS MucPhi (
            nam INT PRIMARY KEY,
            hoc_phi FLOAT
        )
        """)
        
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS DangKyHoc (
            ma_dang_ky_hoc VARCHAR(255) PRIMARY KEY,
            ma_sv VARCHAR(255) REFERENCES SinhVien(ma_sv),
            ma_mon_hoc VARCHAR(255) REFERENCES MonHoc(ma_mon_hoc),
            ky_hoc VARCHAR(255),
            ngay_dang_ky VARCHAR(255)
        )
        """)
