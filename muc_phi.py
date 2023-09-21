class MucPhi:
    def __init__(self, db):
        self.db = db

    def them_muc_phi(self, nam, hoc_phi):
        query = """
        INSERT INTO MucPhi (nam, hoc_phi)
        VALUES (%s, %s)
        """
        self.db.execute_query(query, (nam, hoc_phi))

    def sua_muc_phi(self, nam, hoc_phi):
        query = "UPDATE MucPhi SET hoc_phi=%s WHERE nam=%s"
        self.db.execute_query(query, (hoc_phi, nam))

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

