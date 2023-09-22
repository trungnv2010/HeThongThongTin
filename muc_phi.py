from tabulate import tabulate
class MucPhi:
    def __init__(self, db):
        self.db = db

    def them_muc_phi(self, nam, hoc_phi):
        query = """
        INSERT INTO MucPhi (nam, hoc_phi)
        VALUES (%s, %s)
        """
        self.db.execute_query(query, (nam, hoc_phi))
        self.xem_thong_tin()

    def sua_muc_phi(self, nam, hoc_phi):
        query = "UPDATE MucPhi SET hoc_phi=%s WHERE nam=%s"
        if (hoc_phi):
            self.db.execute_query(query, (hoc_phi, nam))
            self.xem_thong_tin(nam)
        else: 
            print("Không có thông tin nào được chỉnh sửa")

    def xoa_muc_phi(self, nam):
        query = "DELETE FROM MucPhi WHERE nam=%s"
        self.db.execute_query(query, (nam,))

    def lay_hoc_phi(self, nam):
        query = "SELECT hoc_phi FROM MucPhi WHERE nam=%s"
        results = self.db.fetch_query(query, (nam,))
        return results[0][0] if results else None
    
    def muc_phi_ton_tai(self, nam):
        query = "SELECT COUNT(*) FROM MucPhi WHERE nam=%s"
        results = self.db.fetch_query(query, (nam,))
        return results[0][0] > 0

    def lay_hoc_phi_theo_ky(self, ky_hoc):
        # Tách kỳ học để lấy năm
        nam_hoc = ky_hoc.split('-')[0]

        # Truy vấn học phí dựa trên năm
        query = "SELECT hoc_phi FROM MucPhi WHERE nam = %s"
        result = self.db.fetch_query(query, (nam_hoc,))

        # Kiểm tra nếu có kết quả
        if result:
            return result[0]
        else:
            return None


    def xem_thong_tin(self, nam=None):
        query = ""
        results = ""
        if nam == None:
            query = """ 
                SELECT * FROM MucPhi 
            
            """
            results = self.db.fetch_query(query, ())
        else: 
            query = """ 
                SELECT * FROM MucPhi where nam=%s
            
            """
            results = self.db.fetch_query(query, (nam,))
        headers = ["Năm", "Học Phí"]
        print( tabulate(results, headers=headers, tablefmt="grid", floatfmt=(",.0f")))