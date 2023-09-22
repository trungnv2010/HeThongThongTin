from database import Database
from dang_ky_hoc import DangKyHoc
from sinh_vien import SinhVien
from mon_hoc import MonHoc
from muc_phi import MucPhi
from datetime import datetime

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
        print("1. Thiết lập mức học phí")
        print("2. Chỉnh sửa thông tin môn học")
        print("3. Nhập thông tin đăng ký học")
        print("4. Thống kê học phí cho sinh viên")
        print("5. Chỉnh sửa thông tin sinh viên")
        print("0. Thoát")
        
        choice = input("Chọn chức năng: ")
        #Chỉnh sửa học phí
        if choice == "1":
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
                    if (mp.muc_phi_ton_tai(nam)):
                        print(f"Dữ liệu về học phí của năm {nam} đã có. Bạn có muốn tiếp tục không (1- có, 2 - không) ")
                        cont = input("Chọn chức năng: ")
                        if (cont == "1"): 
                            mp.sua_muc_phi(nam, muc_phi)
                        if (cont == "2"): 
                            pass
                    else: 
                        mp.them_muc_phi(nam, muc_phi)
                if (choice1 == "2"): 
                    nam = input("Nhập năm: ")
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
                    nam = input("Nhập năm: ")
                    mp.xoa_muc_phi(nam)
                if (choice1 == "4"):
                    mp.xem_thong_tin()
                if choice1 == "0": 
                    break
        #Thêm sửa xoá thông tin môn học
        if choice == "2":
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
                    so_tin_chi = input("Nhập số tín chỉ: ")
                    he_so = input("Nhập hệ số: ")
                    if (mh.mon_hoc_ton_tai(ma_mon_hoc)):
                        print(f"Dữ liệu của môn học {ma_mon_hoc} đã có. Bạn có muốn tiếp tục không (1- có, 2 - không) ")
                        cont = input("Chọn chức năng: ")
                        if (cont == "1"): 
                            mh.sua_mon_hoc(ma_mon_hoc, ten_mon_hoc, so_tin_chi, he_so)
                        if (cont == "2"): 
                            pass
                    else: 
                        mh.them_mon_hoc(ma_mon_hoc, ten_mon_hoc, so_tin_chi, he_so)
                if (choice1 == "2"): 
                    ma_mon_hoc = input("Nhập mã môn học: ")
                    ten_mon_hoc = input("Nhập tên môn học: ")
                    so_tin_chi = input("Nhập số tín chỉ: ")
                    he_so = input("Nhập hệ số: ")
                    if (not mh.mon_hoc_ton_tai(ma_mon_hoc)):
                        print(f"Dữ liệu của môn học {ma_mon_hoc} chưa có. Bạn có muốn tiếp tục không (1- có, 2 - không) ")
                        cont = input("Chọn chức năng: ")
                        if (cont == "1"): 
                            mh.them_mon_hoc(ma_mon_hoc, ten_mon_hoc, so_tin_chi, he_so)
                        if (cont == "2"): 
                            pass
                    else: 
                        mh.sua_mon_hoc(ma_mon_hoc, ten_mon_hoc, so_tin_chi, he_so)
            
                if (choice1 == "3"): 
                    ma_mon_hoc = input("Nhập mã môn học: ")
                    mh.xoa_mon_hoc(ma_mon_hoc)
                if choice1 == "4": 
                    mh.xem_thong_tin_tat_ca_mon_hoc()
                if choice1 == "0": 
                    break
                   
                    

        # Đăng ký học
        elif choice == "3":  
            while True: 
                print()
                print("\033[1;97;41mĐăng ký học\033[0m")
                print("Vui lòng chọn chức năng bên dưới: ")
                print("1. Đăng ký học")
                print("0. Thoát")
                choice1 = input("Chọn chức năng: ")
                if choice1 == "1": 
                    print("Danh sách các môn bạn có thể đăng ký: ")
                    mh.xem_thong_tin_tat_ca_mon_hoc()
                    ma_sinh_vien = input("Nhập mã sinh viên: ")
                    ma_mon_hoc = input("Nhập mã môn học bạn muốn đăng ký: ")

                    if not sv.sinh_vien_ton_tai(ma_sinh_vien):
                        print("Không có dữ liệu của sinh viên")
                        continue
                    if not mh.mon_hoc_ton_tai(ma_mon_hoc):
                        print("Môn học này không tồn tại trong hệ thống!")
                        continue
                    if dk.da_dang_ky(ma_sinh_vien, ma_mon_hoc):
                        print("Bạn đã đăng ký môn học này trước đó!")
                        continue
                    ky_hoc = input("Nhập kỳ học (VD: 2023-1): ")
                    # ngay_dang_ky = input("Nhập ngày đăng ký (Định dạng YYYY-MM-DD): ")
                    ngay_dang_ky = datetime.now()
                    ngay_dang_ky = ngay_dang_ky.strftime('%Y-%m-%d %H:%M:%S')
                    dk.dang_ky_mon_hoc(ma_sinh_vien, ma_mon_hoc, ky_hoc, ngay_dang_ky)
                    print("Đăng ký thành công!")
                if choice1 == "0": 
                    break

        # Thống kê học phí sinh viên 
        if choice == "4": 
            while True:
                print()
                print("\033[1;97;41mThống kê học phí\033[0m")
                print("Vui lòng chọn chức năng bên dưới: ")
                print("1. Thống kê học phí theo kỳ")
                print("2. Thống kê tổng học phí của sinh viên")
                print("0. Thoát")
                choice1 = input("Chọn chức năng: ")
                if choice1 == "1": 
                    ma_sinh_vien = input("Mã sinh viên: ")
                    ky_hoc = input("Kỳ học: ")
                    sv.thong_ke_hoc_phi_theo_ky(ma_sinh_vien, ky_hoc)
                if choice1 == "2":
                    ma_sinh_vien = input("Mã sinh viên: ")
                    sv.tinh_tong_hoc_phi(ma_sinh_vien)
                if choice1 == "0": 
                    break
        #Thêm sửa xoá thông tin sinh viên
        if choice == "5":
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
                    if (sv.sinh_vien_ton_tai(ma_sinh_vien)):
                        print(f"Dữ liệu của sinh viên {ma_sinh_vien} đã có. Bạn có muốn tiếp tục không (1- có, 2 - không) ")
                        cont = input("Chọn chức năng: ")
                        if (cont == "1"): 
                            sv.sua_sinh_vien(ma_sinh_vien, ho_ten, dia_chi, ngay_sinh, khoa_hoc)
                        if (cont == "2"): 
                            pass
                    else: 
                        sv.them_sinh_vien(ma_sinh_vien, ho_ten, dia_chi, ngay_sinh, khoa_hoc)
                if (choice1 == "2"): 
                    ma_sinh_vien = input("Nhập mã sinh viên: ")
                    ho_ten = input("Nhập họ tên sinh viên: ")
                    dia_chi = input("Địa chỉ: ")
                    ngay_sinh = input("Ngày sinh: ")
                    khoa_hoc = input("Khoá học: ")
                    if (not sv.sinh_vien_ton_tai(ma_sinh_vien)):
                        print(f"Dữ liệu của sinh viên {ma_sinh_vien} chưa có. Bạn có muốn tiếp tục không (1- có, 2 - không) ")
                        cont = input("Chọn chức năng: ")
                        if (cont == "1"): 
                            sv.them_sinh_vien(ma_sinh_vien, ho_ten, dia_chi, ngay_sinh, khoa_hoc)
                        if (cont == "2"): 
                            pass
                    else: 
                        sv.sua_sinh_vien(ma_sinh_vien, ho_ten, dia_chi, ngay_sinh, khoa_hoc)
            
                if (choice1 == "3"):
                    ma_sinh_vien = input("Nhập mã sinh viên: ") 
                    sv.xoa_sinh_vien(ma_sinh_vien)
                if choice1 == "4": 
                    sv.xem_thong_tin()
                if choice1 == "0": 
                    break
        elif choice == "0":
            print("Thoát chương trình.")
            db.close()
            break

