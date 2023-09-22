from tabulate import tabulate
class MonHoc:
    def __init__(self, db):
        self.db = db

    def them_mon_hoc(self, ma_mon_hoc, ten_mon_hoc, thu, ca_hoc, so_tin_chi, he_so):
        query = """
        INSERT INTO MonHoc (ma_mon_hoc, ten_mon_hoc, thu, ca_hoc, so_tin_chi, he_so)
        VALUES (%s, %s, %s, %s, %s,%s,)
        """
        self.db.execute_query(query, (ma_mon_hoc, ten_mon_hoc, so_tin_chi,thu, ca_hoc, he_so))
        self.xem_thong_tin_tat_ca_mon_hoc()

    def sua_mon_hoc(self, ma_mon_hoc, ten_mon_hoc=None,thu=None, ca_hoc=None, so_tin_chi=None, he_so=None):
        fields_to_update = []
        values = []
        if ten_mon_hoc:
            fields_to_update.append("ten_mon_hoc=%s")
            values.append(ten_mon_hoc)
        if thu:
            fields_to_update.append("thu=%s")
            values.append(thu)
        if ca_hoc:
            fields_to_update.append("ca_hoc=%s")
            values.append(ca_hoc)
        if so_tin_chi:
            fields_to_update.append("so_tin_chi=%s")
            values.append(so_tin_chi)
        if he_so:
            fields_to_update.append("he_so=%s")
            values.append(he_so)
        if (fields_to_update):
            query = f"UPDATE MonHoc SET {', '.join(fields_to_update)} WHERE ma_mon_hoc=%s"
            values.append(ma_mon_hoc)
            self.db.execute_query(query, values)
            self.xem_thong_tin_tat_ca_mon_hoc(ma_mon_hoc)
        else: 
            print("Không có thông tin nào được chỉnh sửa")

    def xoa_mon_hoc(self, ma_mon_hoc):
        query = "DELETE FROM MonHoc WHERE ma_mon_hoc=%s"
        self.db.execute_query(query, (ma_mon_hoc,))

    def lay_thong_tin_mon_hoc(self, ma_mon_hoc):
        query = "SELECT * FROM MonHoc WHERE ma_mon_hoc=%s"
        return self.db.fetch_query(query, (ma_mon_hoc,))

    def mon_hoc_ton_tai(self, ma_mon_hoc):
        query = "SELECT COUNT(*) FROM MonHoc WHERE ma_mon_hoc=%s"
        results = self.db.fetch_query(query, (ma_mon_hoc,))
        return results[0][0] > 0
    def xem_thong_tin_tat_ca_mon_hoc(self, ma_mon_hoc=None):
        query = ""
        results = ""
        if ma_mon_hoc == None:
            query = """ 
                SELECT * FROM MonHoc 
            
            """
            results = self.db.fetch_query(query, ())
        else: 
            query = """ 
                SELECT * FROM MonHoc where ma_mon_hoc=%s
            
            """
            results = self.db.fetch_query(query, (ma_mon_hoc,))
    
        headers = ["Mã Môn Học", "Tên Môn Học", "Thứ", "Ca học", "Số Tín Chỉ", "Hệ Số"]
        print(tabulate(results, headers=headers, tablefmt="grid")) 

