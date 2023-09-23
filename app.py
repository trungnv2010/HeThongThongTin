from database import Database
from dang_ky_hoc import DangKyHoc
from sinh_vien import SinhVien
from mon_hoc import MonHoc
from muc_phi import MucPhi
from datetime import datetime


class App:
    def __init__(self):
        self.db = Database(host="localhost", user="root", password="123456")
        self.db.create_database("tuition_fee")
        self.sv = SinhVien(self.db)
        self.mh = MonHoc(self.db)
        self.mp = MucPhi(self.db)
        self.dk = DangKyHoc(self.db)

    def login(self):
        username = input("Nhập tên đăng nhập: ")
        password = input("Nhập mật khẩu: ")
        query = """
        SELECT permission FROM User
        WHERE user_name = %s AND password = %s
        """
        result = self.db.fetch_query(query, (username, password,))
        if result:
            result.append(username)
            return result
        else:
            return [(None,)]

    def main_menu(self):
        while True:
            account_type = self.login()
            if account_type[0][0] == '1':
                self.menu_phong_dao_tao()
            if account_type[0][0] == '2':
                self.menu_sinh_vien(account_type[1])
            if account_type[0][0] == None:
                print("Thông tin đăng nhập không chính xác. Vui lòng thử lại.")

    def menu_phong_dao_tao(self):
        while True:
            print("=== MENU PHÒNG ĐÀO TẠO ===")
            print("1. Thiết lập mức học phí")
            print("2. Chỉnh sửa thông tin môn học")
            print("3. Thống kê học phí cho sinh viên")
            print("4. Chỉnh sửa thông tin sinh viên")
            print("0. Thoát")

            choice = input("Chọn chức năng: ")
            if choice == '1': 
                self.chinh_sua_hoc_phi()
            if choice == '2': 
                self.chinh_sua_thong_tin_mon_hoc()
            if choice == '3':
                self.thong_ke_hoc_phi()
            if choice=='4':
                self.chinh_sua_thong_tin_sinh_vien()
            if choice == '0':
                break

    def menu_sinh_vien(self, ma_sv):
        while True:
            print("=== MENU SINH VIÊN ===")
            print("1. Xem thông tin cá nhân")
            print("2. Xem học phí")
            print("3. Nhập thông tin đăng ký học")
            print("0. Thoát")

            choice = input("Chọn chức năng: ")
            if choice== '1': 

                self.xem_thong_tin_ca_nhan(ma_sv)
            if choice == '2':
                self.thong_ke_hoc_phi(ma_sv)
            if choice == '3': 
                self.dang_ky_hoc(ma_sv)
            if choice == '0':
                break

    def chinh_sua_hoc_phi(self): 
        while True:
            print()
            print("\033[1;97;41mThiết lập mức học phí\033[0m")
            print("Vui lòng chọn chức năng bên dưới: ")
            print("1. Thêm")
            print("2. Sửa")
            print("3. Xoá")
            print("4. Xem thông tin")
            print("0. Thoát")
            choice1 = input("Chọn chức năng: ")
            
            if (choice1 == "1"): 
                nam = input("Nhập năm: ")
                muc_phi = input("Nhập mức học phí: ")
                if (self.mp.muc_phi_ton_tai(nam)):
                    print(f"Dữ liệu về học phí của năm {nam} đã có. Bạn có muốn tiếp tục không (1- có, 2 - không) ")
                    cont = input("Chọn chức năng: ")
                    if (cont == "1"): 
                        self.mp.sua_muc_phi(nam, muc_phi)
                    if (cont == "2"): 
                        pass
                else: 
                    self.mp.them_muc_phi(nam, muc_phi)
            if (choice1 == "2"): 
                nam = input("Nhập năm: ")
                hoc_phi = input("Nhập mức học phí: ")
                if (not self.mp.muc_phi_ton_tai(nam)):
                    print(f"Dữ liệu về học phí của năm {nam} chưa có. Bạn có muốn tiếp tục không (1- có, 2 - không) ")
                    cont = input("Chọn chức năng: ")
                    if (cont == "1"): 
                        self.mp.them_muc_phi(nam, muc_phi)
                    if (cont == "2"): 
                        pass
                else: 
                    self.mp.sua_muc_phi(nam, hoc_phi)
        
            if (choice1 == "3"): 
                nam = input("Nhập năm: ")
                self.mp.xoa_muc_phi(nam)
            if (choice1 == "4"):
                self.mp.xem_thong_tin()
            if choice1 == "0": 
                break
    def chinh_sua_thong_tin_mon_hoc(self):
        while True:
            print()
            print("\033[1;97;41mChỉnh sửa thông tin môn học\033[0m")
            print("Vui lòng chọn chức năng bên dưới: ")
            print("1. Thêm")
            print("2. Sửa")
            print("3. Xoá")
            print("4. Xem thông tin ")
            print("0. Thoát")
            choice1 = input("Chọn chức năng: ")
            if (choice1 == "1"): 
                ma_mon_hoc = input("Nhập mã môn học: ")
                ten_mon_hoc = input("Nhập tên môn học: ")
                thu = input("Nhập thứ: ")
                ca_hoc = input("Nhập ca học: ")
                so_tin_chi = input("Nhập số tín chỉ: ")
                he_so = input("Nhập hệ số: ")
                if (self.mh.mon_hoc_ton_tai(ma_mon_hoc)):
                    print(f"Dữ liệu của môn học {ma_mon_hoc} đã có. Bạn có muốn tiếp tục không (1- có, 2 - không) ")
                    cont = input("Chọn chức năng: ")
                    if (cont == "1"): 
                        self.mh.sua_mon_hoc(ma_mon_hoc, ten_mon_hoc, thu, ca_hoc, so_tin_chi, he_so)
                    if (cont == "2"): 
                        pass
                else: 
                    self.mh.them_mon_hoc(ma_mon_hoc, ten_mon_hoc, thu, ca_hoc, so_tin_chi, he_so)
            if (choice1 == "2"): 
                ma_mon_hoc = input("Nhập mã môn học: ")
                ten_mon_hoc = input("Nhập tên môn học: ")
                thu = input("Nhập thứ: ")
                ca_hoc = input("Nhập ca học: ")
                so_tin_chi = input("Nhập số tín chỉ: ")
                he_so = input("Nhập hệ số: ")
                if (not self.mh.mon_hoc_ton_tai(ma_mon_hoc)):
                    print(f"Dữ liệu của môn học {ma_mon_hoc} chưa có. Bạn có muốn tiếp tục không (1- có, 2 - không) ")
                    cont = input("Chọn chức năng: ")
                    if (cont == "1"): 
                        self.mh.them_mon_hoc(ma_mon_hoc, ten_mon_hoc, thu, ca_hoc, so_tin_chi, he_so)
                    if (cont == "2"): 
                        pass
                else: 
                    self.mh.sua_mon_hoc(ma_mon_hoc, ten_mon_hoc, thu, ca_hoc, so_tin_chi, he_so)
        
            if (choice1 == "3"): 
                ma_mon_hoc = input("Nhập mã môn học: ")
                self.mh.xoa_mon_hoc(ma_mon_hoc)
            if choice1 == "4": 
                self.mh.xem_thong_tin_tat_ca_mon_hoc()
            if choice1 == "0": 
                break
    def xem_thong_tin_ca_nhan(self, ma_sinh_vien):
        self.sv.xem_thong_tin(ma_sinh_vien)
    
    def thong_ke_hoc_phi(self, ma_sinh_vien=None): 
        while True:
            print()
            print("\033[1;97;41mThống kê học phí\033[0m")
            print("Vui lòng chọn chức năng bên dưới: ")
            print("1. Thống kê học phí theo kỳ")
            print("2. Thống kê tổng học phí của sinh viên")
            print("0. Thoát")
            choice1 = input("Chọn chức năng: ")
            if choice1 == "1": 
                if (ma_sinh_vien == None):
                    ma_sinh_vien = input("Mã sinh viên: ")
                    ky_hoc = input("Kỳ học: ")
                    self.sv.thong_ke_hoc_phi_theo_ky(ma_sinh_vien, ky_hoc)
                    ma_sinh_vien=None
                else:
                    ky_hoc = input("Kỳ học: ")
                    self.sv.thong_ke_hoc_phi_theo_ky(ma_sinh_vien, ky_hoc)
            if choice1 == "2":
                if (ma_sinh_vien == None):
                    ma_sinh_vien = input("Mã sinh viên: ")
                    self.sv.tinh_tong_hoc_phi(ma_sinh_vien)
                    ma_sinh_vien=None
                else: 
                    self.sv.tinh_tong_hoc_phi(ma_sinh_vien)
            if choice1 == "0": 
                break

    def dang_ky_hoc(self, ma_sinh_vien): 
         while True: 
            print()
            print("\033[1;97;41mĐăng ký học\033[0m")
            print("Vui lòng chọn chức năng bên dưới: ")
            print("1. Đăng ký học")
            print("2. Huỷ đăng ký học")
            print("0. Thoát")
            choice1 = input("Chọn chức năng: ")
            if choice1 == "1": 
                print("Danh sách các môn bạn có thể đăng ký: ")
                self.mh.xem_thong_tin_tat_ca_mon_hoc()
                # ma_sinh_vien = input("Nhập mã sinh viên: ")
                ma_mon_hoc = input("Nhập mã môn học bạn muốn đăng ký: ")

                # if not self.sv.sinh_vien_ton_tai(ma_sinh_vien):
                #     print("Không có dữ liệu của sinh viên")
                #     continue
                if not self.mh.mon_hoc_ton_tai(ma_mon_hoc):
                    print("Môn học này không tồn tại trong hệ thống!")
                    continue
                if self.dk.da_dang_ky(ma_sinh_vien, ma_mon_hoc):
                    print("Bạn đã đăng ký môn học này trước đó!")
                    continue
                ky_hoc = input("Nhập kỳ học (VD: 2023-1): ")
                # ngay_dang_ky = input("Nhập ngày đăng ký (Định dạng YYYY-MM-DD): ")
                ngay_dang_ky = datetime.now()
                ngay_dang_ky = ngay_dang_ky.strftime('%Y-%m-%d %H:%M:%S')
                self.dk.dang_ky_mon_hoc(ma_sinh_vien, ma_mon_hoc, ky_hoc, ngay_dang_ky)
                print("Đăng ký thành công!")
                print(f"Các môn sinh viên {ma_sinh_vien} đã đăng ký trong kỳ {ky_hoc}: ")
                self.mh.xem_thong_tin_cac_mon_theo_ky(ma_sinh_vien, ky_hoc)
            if choice1 == '2':
                ky_hoc = input("Nhập kỳ học (VD: 2023-1): ")
                self.mh.xem_thong_tin_cac_mon_theo_ky(ma_sinh_vien, ky_hoc)
                ma_mon_hoc = input("Nhập mã môn học bạn muốn huỷ đăng ký: ")
                if not self.dk.da_dang_ky(ma_sinh_vien, ma_mon_hoc, ky_hoc):
                    print("Bạn chưa đăng ký môn học trong kỳ này!")
                    continue
                # ngay_dang_ky = input("Nhập ngày đăng ký (Định dạng YYYY-MM-DD): ")
                self.dk.huy_dang_ky(ma_sinh_vien, ma_mon_hoc, ky_hoc)
                print(f"Các môn sinh viên {ma_sinh_vien} đã đăng ký trong kỳ {ky_hoc}: ")
                self.mh.xem_thong_tin_cac_mon_theo_ky(ma_sinh_vien, ky_hoc)
            if choice1 == "0": 
                break

    def chinh_sua_thong_tin_sinh_vien(self):
        while True:
            print()
            print("\033[1;97;41mChỉnh sửa thông tin sinh viên\033[0m")
            print("Vui lòng chọn chức năng bên dưới: ")
            print("1. Thêm")
            print("2. Sửa")
            print("3. Xoá")
            print("4. Xem thông tin ")
            print("0. Thoát")
            choice1 = input("Chọn chức năng: ")
            if (choice1 == "1"): 
                ma_sinh_vien = input("Nhập mã sinh viên: ")
                ho_ten = input("Nhập họ tên sinh viên: ")
                dia_chi = input("Địa chỉ: ")
                ngay_sinh = input("Ngày sinh: ")
                khoa_hoc = input("Khoá học: ")
                if (self.sv.sinh_vien_ton_tai(ma_sinh_vien)):
                    print(f"Dữ liệu của sinh viên {ma_sinh_vien} đã có. Bạn có muốn tiếp tục không (1- có, 2 - không) ")
                    cont = input("Chọn chức năng: ")
                    if (cont == "1"): 
                        self.sv.sua_sinh_vien(ma_sinh_vien, ho_ten, dia_chi, ngay_sinh, khoa_hoc)
                    if (cont == "2"): 
                        pass
                else: 
                    self.sv.them_sinh_vien(ma_sinh_vien, ho_ten, dia_chi, ngay_sinh, khoa_hoc)
            if (choice1 == "2"): 
                ma_sinh_vien = input("Nhập mã sinh viên: ")
                ho_ten = input("Nhập họ tên sinh viên: ")
                dia_chi = input("Địa chỉ: ")
                ngay_sinh = input("Ngày sinh: ")
                khoa_hoc = input("Khoá học: ")
                if (not self.sv.sinh_vien_ton_tai(ma_sinh_vien)):
                    print(f"Dữ liệu của sinh viên {ma_sinh_vien} chưa có. Bạn có muốn tiếp tục không (1- có, 2 - không) ")
                    cont = input("Chọn chức năng: ")
                    if (cont == "1"): 
                        self.sv.them_sinh_vien(ma_sinh_vien, ho_ten, dia_chi, ngay_sinh, khoa_hoc)
                    if (cont == "2"): 
                        pass
                else: 
                    self.sv.sua_sinh_vien(ma_sinh_vien, ho_ten, dia_chi, ngay_sinh, khoa_hoc)
        
            if (choice1 == "3"):
                ma_sinh_vien = input("Nhập mã sinh viên: ") 
                self.sv.xoa_sinh_vien(ma_sinh_vien)
            if choice1 == "4": 
                self.sv.xem_thong_tin()
            if choice1 == "0": 
                break