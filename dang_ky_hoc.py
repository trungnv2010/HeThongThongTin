import uuid
class DangKyHoc:
    def __init__(self, db):
        self.db = db

    def tao_ma_dang_ky_hoc(self):
        return str(uuid.uuid4().hex)

    def dang_ky_mon_hoc(self, ma_sv, ma_mon_hoc, ky_hoc, ngay_dang_ky):
        ma_dang_ky_hoc = self.tao_ma_dang_ky_hoc()
        query = """
        INSERT INTO DangKyHoc (ma_dang_ky_hoc, ma_sv, ma_mon_hoc, ky_hoc, ngay_dang_ky)
        VALUES (%s, %s, %s, %s, %s)
        """
        self.db.execute_query(query, (ma_dang_ky_hoc, ma_sv, ma_mon_hoc, ky_hoc, ngay_dang_ky))

    def tinh_hoc_phi_ky(self, ma_sv, ky_hoc):
        query = """
        SELECT SUM(m.so_tin_chi * m.he_so * mp.hoc_phi) as hoc_phi_ky
        FROM DangKyHoc d
        JOIN MonHoc m ON d.ma_mon_hoc = m.ma_mon_hoc
        JOIN MucPhi mp ON YEAR(d.ngay_dang_ky) = mp.nam
        WHERE d.ma_sv = %s AND d.ky_hoc = %s
        """
        results = self.db.fetch_query(query, (ma_sv, ky_hoc))
        return results[0][0] if results else 0

    def thong_ke_hoc_phi(self, ma_sv):
        query = """
        SELECT d.ky_hoc, COUNT(d.ma_mon_hoc) as so_mon, SUM(m.so_tin_chi) as so_tin_chi, 
               SUM(m.so_tin_chi * m.he_so * mp.hoc_phi) as hoc_phi_ky
        FROM DangKyHoc d
        JOIN MonHoc m ON d.ma_mon_hoc = m.ma_mon_hoc
        JOIN MucPhi mp ON YEAR(d.ngay_dang_ky) = mp.nam
        WHERE d.ma_sv = %s
        GROUP BY d.ky_hoc
        """
        return self.db.fetch_query(query, (ma_sv,))

    def da_dang_ky(self, ma_sv, ma_mon_hoc, ky_hoc=None):
        result = ""
        query = ""
        if (not ky_hoc):
            query = """
            SELECT COUNT(*) FROM DangKyHoc
            WHERE ma_sv=%s AND ma_mon_hoc=%s
            """
            results = self.db.fetch_query(query, (ma_sv, ma_mon_hoc))
        else:
            query = """
            SELECT COUNT(*) FROM DangKyHoc
            WHERE ma_sv=%s AND ma_mon_hoc=%s and ky_hoc=%s
            """
            results = self.db.fetch_query(query, (ma_sv, ma_mon_hoc, ky_hoc))
        return results[0][0] > 0


    def huy_dang_ky(self, ma_sv, ma_mon_hoc, ky_hoc):
    
        confirm = input("Bạn có chắc chắn muốn hủy đăng ký môn học này không? (y/n): ")
        
        if confirm.lower() == 'y':
            try:
                # Thực hiện truy vấn SQL
                self.db.execute_query("DELETE FROM DangKyHoc WHERE ma_sv = %s AND ma_mon_hoc = %s AND ky_hoc = %s", (ma_sv, ma_mon_hoc, ky_hoc))
                
                print("Hủy đăng ký thành công!")
            except Exception as e:
                print("Có lỗi xảy ra:", e)
                self.conn.rollback()
