class SinhVien:
    def __init__(self, db):
        self.db = db

    def them_sinh_vien(self, ma_sv, ho_ten, dia_chi, ngay_sinh, khoa_hoc):
        query = """
        INSERT INTO SinhVien (ma_sv, ho_ten, dia_chi, ngay_sinh, khoa_hoc)
        VALUES (%s, %s, %s, %s, %s)
        """
        self.db.execute_query(query, (ma_sv, ho_ten, dia_chi, ngay_sinh, khoa_hoc))

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
        query = f"UPDATE SinhVien SET {', '.join(fields_to_update)} WHERE ma_sv=%s"
        values.append(ma_sv)
        self.db.execute_query(query, values)

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

