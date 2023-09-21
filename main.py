from database import Database
from dang_ky_hoc import DangKyHoc
from sinh_vien import SinhVien
from mon_hoc import MonHoc
from muc_phi import MucPhi

if __name__ == "__main__":
    # Connect to the database
    db = Database(host="localhost", user="root", password="123456")
    db.create_database("tuition_fee")
    sv = SinhVien(db)
    mh = MonHoc(db)
    mp = MucPhi(db)
    dk = DangKyHoc(db)

    while True:
        print("=== MENU ===")
        print("1. Thiết lập mức đơn vị phí")
        print("2. Nhập thông tin môn học")
        print("3. Nhập thông tin đăng ký học và tính học phí")
        print("4. Thống kê học phí cho sinh viên")
        print("5. Thêm/Sửa/Xoá thông tin sinh viên")
        print("6. Thêm/Sửa/Xoá thông tin môn học")
        print("0. Thoát")
        
        choice = input("Chọn chức năng: ")

        if choice == "1":
            print("Vui lòng chọn chức năng bên dưới: ")
            print("1. Thêm")
            print("2. Sửa")
            print("3. Xoá")
            choice1 = input("Chọn chức năng: ")
            nam = input("Nhập năm: ")
            if (choice1 == "1"): 
                muc_phi = input("Nhập mức học phí: ")
                if (mp.muc_phi_ton_tai(nam)):
                    print(f"Dữ liệu về học phí của năm {nam} đã có. Bạn có muốn tiếp tục không (1- có, 2 - không) ")
                    cont = input("Chọn chức năng: ")
                    if (cont == "1"): 
                        mp.sua_muc_phi(nam, muc_phi)
                    if (cont == "2"): 
                        pass
                else: 
                    mp.them_muc_phi(nam, hoc_phi)
            if (choice1 == "2"): 
                hoc_phi = input("Nhập mức học phí: ")
                if (not mp.muc_phi_ton_tai(nam)):
                    print(f"Dữ liệu về học phí của năm {nam} chưa có. Bạn có muốn tiếp tục không (1- có, 2 - không) ")
                    cont = input("Chọn chức năng: ")
                    if (cont == "1"): 
                        mp.them_muc_phi(nam, muc_phi)
                    if (cont == "2"): 
                        pass
                else: 
                    mp.sua_muc_phi(nam, hoc_phi)
        
            if (choice1 == "3"): 
                mp.xoa_muc_phi(nam)


        elif choice == "0":
            print("Thoát chương trình.")
            db.close()
            break

