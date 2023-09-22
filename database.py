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
            thu VARCHAR(2),
            ca_hoc VARCHAR(2),
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

        # Tạo dữ liệu cho bảng sinh viên 

        self.cursor.execute("SELECT COUNT(*) FROM SinhVien")
        count = self.cursor.fetchone()[0]
        if count == 0:
            query = "INSERT INTO SinhVien (ma_sv, ho_ten, dia_chi, ngay_sinh, khoa_hoc) VALUES (%s, %s, %s, %s, %s)"
            data = [
                ('SV01', 'Nguyễn Văn An', 'Hà Nội', '2003-01-01', '34'),
                ('SV02', 'Lê Thị Bình', 'Hải Phòng', '2003-02-02', '34'),
                ('SV03', 'Phạm Văn Cảnh', 'Đà Nẵng', '2003-03-03', '34'),
                ('SV04', 'Trần Thị Dung', 'Cần Thơ', '2003-04-04', '34'),
                ('SV05', 'Hoàng Văn Em', 'Huế', '2003-05-05', '34'),
                ('SV06', 'Đặng Thị Phương', 'Nha Trang', '2003-06-06', '34'),
                ('SV07', 'Bùi Văn Giang', 'Đà Lạt', '2003-07-07', '34'),
                ('SV08', 'Vũ Thị Hoa', 'Vinh', '2003-08-08', '34'),
                ('SV09', 'Lê Văn Hùng', 'Quảng Ninh', '2003-09-09', '34'),
                ('SV10', 'Phạm Thị Kim', 'Quảng Bình', '2003-10-10', '34'),
                ('SV11', 'Nguyễn Văn Lâm', 'Quảng Trị', '2003-11-11', '34'),
                ('SV12', 'Trần Văn Minh', 'Quảng Ngãi', '2003-12-12', '34'),
                ('SV13', 'Hoàng Thị Nga', 'Bình Định', '2001-01-01', '34'),
                ('SV14', 'Dương Văn Phúc', 'Bắc Ninh', '2001-02-02', '34'),
                ('SV15', 'Ngô Thị Quỳnh', 'Nam Định', '2001-03-03', '34')
                
            ]
            self.cursor.executemany(query, data)
        

        # Tạo dữ liệu cho bảng mức phí
        self.cursor.execute("SELECT COUNT(*) FROM MucPhi")
        count = self.cursor.fetchone()[0]
        if count == 0: 
            query = "INSERT INTO MucPhi (nam, hoc_phi ) VALUES (%s, %s)"
            data = [
                ('2021', '400000' ),
                ('2022', '450000' ),
                ('2023', '500000' ),
                ('2024', '550000' )
            ]
            self.cursor.executemany(query, data)

        # Tạo dữ liệu cho bảng môn học 
        self.cursor.execute("SELECT COUNT(*) FROM MonHoc")
        count = self.cursor.fetchone()[0]
        if count == 0:
            query = "INSERT INTO MonHoc (ma_mon_hoc, ten_mon_hoc, thu, ca_hoc, so_tin_chi, he_so) VALUES (%s, %s, %s, %s, %s, %s)"
            data = [
                ('CS121', 'Ngôn Ngữ Lập Trình', '2', '3', 3, 1.6),
                ('CS122', 'Cấu Trúc Dữ Liệu và Giải Thuật', '3', '2', 4, 1.8),
                ('CS123', 'Hệ Điều Hành', '5', '1', 3, 1.5),
                ('CS124', 'Lập Trình Hướng Đối Tượng', '4', '3', 3, 1.7),
                ('CS125', 'Cơ Sở Dữ Liệu', '2', '1', 4, 1.9),
                ('CS126', 'Mạng Máy Tính', '3', '3', 3, 1.6),
                ('CS127', 'Phân Tích và Thiết Kế Hệ Thống', '4', '2', 3, 1.5),
                ('CS128', 'Kỹ Thuật Lập Trình', '5', '2', 2, 1.4),
                ('CS129', 'Lý Thuyết Đồ Thị', '3', '1', 2, 1.3),
                ('CS130', 'Trí Tuệ Nhân Tạo', '2', '3', 3, 1.7),
                ('CS131', 'Thực Hành Cơ Sở Dữ Liệu', '5', '3', 1, 1.2),
                ('CS132', 'Lập Trình Web', '4', '1', 3, 1.8),
                ('CS133', 'Lập Trình Di Động', '3', '2', 3, 1.7),
                ('CS134', 'Phân Tích và Thiết Kế Thuật Toán', '2', '2', 3, 1.9),
                ('CS135', 'Bảo Mật Thông Tin', '5', '1', 3, 1.6)
                
            ]
            self.cursor.executemany(query, data)
        self.connection.commit()