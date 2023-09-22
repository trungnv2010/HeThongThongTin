from muc_phi import MucPhi
from tabulate import tabulate

class SinhVien:
    def __init__(self, db):
        self.db = db
        self.muc_phi = MucPhi(db)
        

    def them_sinh_vien(self, ma_sv, ho_ten, dia_chi, ngay_sinh, khoa_hoc):
        query = """
        INSERT INTO SinhVien (ma_sv, ho_ten, dia_chi, ngay_sinh, khoa_hoc)
        VALUES (%s, %s, %s, %s, %s)
        """
        self.db.execute_query(query, (ma_sv, ho_ten, dia_chi, ngay_sinh, khoa_hoc))
        self.xem_thong_tin()

    def sua_sinh_vien(self, ma_sv, ho_ten=None, dia_chi=None, ngay_sinh=None, khoa_hoc=None):
        fields_to_update = []
        values = []
        if ho_ten:
            fields_to_update.append("ho_ten=%s")
            values.append(ho_ten)
        if dia_chi:
            fields_to_update.append("dia_chi=%s")
            values.append(dia_chi)
        if ngay_sinh:
            fields_to_update.append("ngay_sinh=%s")
            values.append(ngay_sinh)
        if khoa_hoc:
            fields_to_update.append("khoa_hoc=%s")
            values.append(khoa_hoc)
        if (fields_to_update):
            query = f"UPDATE SinhVien SET {', '.join(fields_to_update)} WHERE ma_sv=%s"
            values.append(ma_sv)
            self.db.execute_query(query, values)
            self.xem_thong_tin(ma_sv)
        else: 
            print("Không có thông tin nào được chỉnh sửa")
    def xoa_sinh_vien(self, ma_sv):
        query = "DELETE FROM SinhVien WHERE ma_sv=%s"
        self.db.execute_query(query, (ma_sv,))

    def lay_thong_tin_sinh_vien(self, ma_sv):
        query = "SELECT * FROM SinhVien WHERE ma_sv=%s"
        return self.db.fetch_query(query, (ma_sv,))
    
    def sinh_vien_ton_tai(self, ma_sv):
        query = "SELECT COUNT(*) FROM SinhVien WHERE ma_sv=%s"
        results = self.db.fetch_query(query, (ma_sv,))
        return results[0][0] > 0 

    def thong_ke_hoc_phi_theo_ky(self, ma_sv, ky_hoc):
        # Kiểm tra sự tồn tại của sinh viên
        student = self.sinh_vien_ton_tai(ma_sv)
        if not student:
            print(f"Không tìm thấy sinh viên với mã {ma_sv}.")
            return
        # Kiểm tra môn học đã đăng ký
        query = """
                SELECT COUNT(*)
                FROM DangKyHoc AS dk
                WHERE dk.ma_sv = %s AND dk.ky_hoc = %s
                """
        registered_courses = self.db.fetch_query(query, (ma_sv, ky_hoc,))
        if registered_courses[0][0] <= 0:
            print(f"Sinh viên {ma_sv} không đăng ký môn học nào trong kỳ {ky_hoc}.")
            return

        # Lấy học phí theo kỳ học
        hoc_phi = self.muc_phi.lay_hoc_phi_theo_ky(ky_hoc)
        if hoc_phi is None:
            print(f"Không thể tra cứu học phí cho kỳ {ky_hoc}.")
            return
        # Truy vấn thông tin môn học và học phí từng môn mà sinh viên đã đăng ký trong kỳ học cụ thể
        query ="""
            SELECT
                mh.ma_mon_hoc,
                mh.ten_mon_hoc,
                mh.so_tin_chi,
                mh.he_so,
                mh.so_tin_chi * mp.hoc_phi * mh.he_so AS hoc_phi_mon
            FROM
                DangKyHoc AS dk
            JOIN
                MonHoc AS mh ON dk.ma_mon_hoc = mh.ma_mon_hoc
            JOIN
                MucPhi AS mp ON SUBSTRING_INDEX(dk.ky_hoc, '-', 1) = mp.nam
            WHERE
                dk.ma_sv = %s AND dk.ky_hoc = %s
            """

        data = self.db.fetch_query(query, (ma_sv, ky_hoc))
        # In kết quả
        tong_hoc_phi = 0
        print(f"Sinh viên {ma_sv} đã đăng ký các môn sau trong kỳ {ky_hoc}:")
        # print("Mã môn", "Tên môn", "Số tín chỉ", "Học phí môn")
        headers = ["STT", "Mã Môn Học", "Tên Môn Học", "Số Tín Chỉ", "Hệ Số", "Học Phí"]
        data = [list(row) for row in data]
        for row in data:
            # print(row[0], row[1], row[2], row[3])
            tong_hoc_phi += row[4]
            row[-1] = self.format_vnd(row[-1])
        data_with_stt = [(index+1, *row) for index, row in enumerate(data)]
        print(tabulate(data_with_stt, headers=headers, tablefmt='grid'))
        tong_hoc_phi = self.format_vnd(tong_hoc_phi)
        print(f"\nTổng học phí cả kỳ: {tong_hoc_phi}")

    def tinh_tong_hoc_phi(self, ma_sv):
        query = """
                SELECT
                    dk.ky_hoc,
                    COUNT(dk.ma_mon_hoc) as so_mon,
                    SUM(mh.so_tin_chi) as tong_so_tin_chi,
                    SUM(mh.so_tin_chi * mp.hoc_phi * mh.he_so) AS hoc_phi_ky
                FROM 
                    DangKyHoc AS dk
                JOIN 
                    MonHoc AS mh ON dk.ma_mon_hoc = mh.ma_mon_hoc
                JOIN 
                    MucPhi AS mp ON SUBSTRING(dk.ky_hoc, 1, 4) = mp.nam
                WHERE 
                    dk.ma_sv = %s
                GROUP BY 
                    dk.ky_hoc
                """
        results = self.db.fetch_query(query, (ma_sv,))

        if not results:
            print(f"Sinh viên với mã {ma_sv} không có dữ liệu học phí.")
            return None

        # In bảng tổng kết
        
        tong_so_mon = 0
        tong_tin_chi = 0
        tong_hoc_phi = 0
        results = [list(row) for row in results]
        for row in results: 
            tong_so_mon += row[1]
            tong_tin_chi += row[2]
            tong_hoc_phi += row[3]
            row[-1] = self.format_vnd(row[-1])
        tong_hoc_phi = self.format_vnd(tong_hoc_phi)
        result_with_stt = [(index+1, *row) for index, row in enumerate(results)]
        headers = ["STT", "Kì học", "Tổng số môn ", "Tổng số Tín Chỉ", "Tổng Học Phí"]
        print(tabulate(result_with_stt, headers=headers, tablefmt='grid'))
        print(f"Tổng số môn đã học: {tong_so_mon} ")
        print(f"Tổng tín chỉ đã học: {tong_tin_chi} ")
        print(f"Tổng học phí: {tong_hoc_phi} ")
    
    def format_vnd(self, value):
        return "{:,.0f} VNĐ".format(value).replace(",", ".")

    def xem_thong_tin(self, ma_sv = None): 
        query = ""
        results = ""
        if ma_sv == None:
            query = """ 
                SELECT * FROM SinhVien 
            
            """
            results = self.db.fetch_query(query, ())
        else: 
            query = """ 
                SELECT * FROM SinhVien where ma_sv=%s
            
            """
            results = self.db.fetch_query(query, (ma_sv,))
        headers = ["Mã SV", "Họ và Tên", "Địa Chỉ", "Ngày Sinh", "Khoá Học"]
        print(tabulate(results, headers=headers, tablefmt="grid")) 