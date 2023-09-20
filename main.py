import mysql.connector
from datetime import datetime

# Kết nối với MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123456",
    database="tuition_fee"
)
cursor = conn.cursor()

def setup_database():
    # Tạo bảng đơn vị phí
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS fee_units (
        year INT PRIMARY KEY,
        fee_per_unit INT
    )
    """)
    
    # Tạo bảng môn học
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS courses (
        course_code VARCHAR(20) PRIMARY KEY,
        course_name VARCHAR(255),
        credits INT,
        factor FLOAT
    )
    """)

    # Tạo bảng thông tin sinh viên 
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        student_code VARCHAR(20) PRIMARY KEY,
        student_name VARCHAR(100),
        batch INT
    )
    """)
    
    # Tạo bảng đăng ký học
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS enroll (
        enroll_code INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
        student_code VARCHAR(20),
        course_code VARCHAR(20),
        semester VARCHAR(20),
        enroll_date VARCHAR(200),
        FOREIGN KEY(course_code) REFERENCES courses(course_code),
        FOREIGN KEY(student_code) REFERENCES students(student_code)
    )
    """)

    

def set_fee_per_unit():
    year = int(input("Nhập năm: "))
    fee = float(input("Nhập mức đơn vị phí: "))
    # Kiểm tra năm đã tồn tại hay chưa
    cursor.execute("SELECT * FROM fee_units WHERE year = %s", (year,))
    existing = cursor.fetchone()
    
    if existing:
        # Nếu năm đã tồn tại, cập nhật phí cho năm đó
        cursor.execute("UPDATE fee_units SET fee_per_unit = %s WHERE year = %s", (fee, year))
        print(f"Mức phí cho năm {year} đã được cập nhật.")
    else:
        # Nếu năm chưa tồn tại, thêm mức phí mới
        cursor.execute("INSERT INTO fee_units (year, fee_per_unit) VALUES (%s, %s)", (year, fee))
        print(f"Mức phí cho năm {year} đã được thiết lập.")
    conn.commit()

def add_course():
    code = input("Mã môn: ")
    name = input("Tên môn: ")
    credits = int(input("Số tín chỉ: "))
    factor = float(input("Hệ số: "))

    # Kiểm tra môn đã tồn tại hay chưa
    cursor.execute("SELECT * FROM courses WHERE course_code = %s", (code,))
    existing = cursor.fetchone()
    
    if existing:
        # Nếu môn đã tồn tại, cập nhật thông tin cho môn đó
        cursor.execute("UPDATE courses SET course_name = %s, credits = %s, factor = %s WHERE course_code = %s", (name, credits, factor, code))
        print(f"Thông tin môn học với mã {code} đã được cập nhật.")
    else:
        # Nếu môn chưa tồn tại, thêm môn mới
        cursor.execute("INSERT INTO courses (course_code, course_name, credits, factor) VALUES (%s, %s, %s, %s)", (code, name, credits, factor))
        print(f"Môn học với mã {code} đã được thêm vào.")
    

    conn.commit()

def add_student():
    student_code = input("Mã sinh viên: ")
    student_name = input("Tên sinh viên: ")
    batch = input("Khoá: ")
    # Kiểm tra mã sinh viên đã tồn tại hay chưa
    cursor.execute("SELECT * FROM students WHERE student_code = %s", (student_code,))
    existing = cursor.fetchone()
    
    if existing:
        # Nếu mã sinh viên đã tồn tại, yêu cầu nhập lại
        print(f"Mã sinh viên {student_code} đã tồn tại trong hệ thống. Vui lòng nhập lại.")
    else:
        # Nếu mã sinh viên chưa tồn tại, thêm mã sinh viên mới
        cursor.execute("INSERT INTO students (student_code, student_name, batch) VALUES (%s, %s, %s)", (student_code, student_name, batch))
        print(f"Mã sinh viên {student_code} đã được thêm vào")
    

    conn.commit()

def enroll_course():
    semester = input("Nhập kì học: ")
    code = input("Mã môn: ")
    student_code = input("Mã sinh viên: ")
    enroll_date = datetime.now()
    enroll_date = enroll_date.strftime('%Y-%m-%d %H:%M:%S')

     # Kiểm tra môn đã tồn tại hay chưa
    cursor.execute("SELECT * FROM enroll WHERE course_code = %s and student_code = %s", (code,student_code))
    existing = cursor.fetchone()
    
    if existing:
        # Nếu môn đã tồn tại, cập nhật thông tin cho môn đó
        print(f"Bạn đã đăng ký môn {code} rồi! ")
    else:
        # Nếu môn chưa tồn tại, thêm môn mới
        cursor.execute("INSERT INTO enroll (student_code, course_code, semester, enroll_date) VALUES (%s, %s, %s, %s)", (student_code, code, semester, enroll_date))
        print(f"Đăng ký môn {code} thành công.")
    conn.commit()

def calculate_fee():
    # Lấy phí theo đơn vị tín chỉ
    year = int(input("Nhập năm để lấy mức phí: "))
    cursor.execute("SELECT fee_per_unit FROM fee_units WHERE year = %s", (year,))
    fee_per_unit = cursor.fetchone()[0]
    
    # Tính phí cho mỗi kì
    cursor.execute("SELECT semester, COUNT(course_code), SUM(credits * factor) FROM student_courses JOIN courses ON student_courses.course_code = courses.course_code GROUP BY semester")
    
    total_courses = 0
    total_credits = 0
    total_fee = 0
    for idx, (semester, num_courses, total_credit) in enumerate(cursor, 1):
        fee = total_credit * fee_per_unit
        print(f"STT: {idx} | Kì học: {semester} | Tổng số môn: {num_courses} | Tổng số tín chỉ: {total_credit} | Học phí: {fee}")
        
        total_courses += num_courses
        total_credits += total_credit
        total_fee += fee
        
    print(f"\nTổng cộng - Số môn: {total_courses} | Tổng số tín chỉ: {total_credits} | Tổng học phí: {total_fee}")

if __name__ == "__main__":
    setup_database()
    
    while True:
        print("\nChọn chức năng:")
        print("1. Thiết lập mức đơn vị phí")
        print("2. Nhập thông tin môn học")
        print("3. Đăng ký môn học cho kì học")
        print("4. Tính tổng học phí")
        print("5. Nhập thông tin sinh viên")
        print("6. Thoát")

        choice = int(input("Nhập lựa chọn của bạn: "))

        if choice == 1:
            set_fee_per_unit()
        elif choice == 2:
            add_course()
        elif choice == 3:
            enroll_course()
        elif choice == 4:
            calculate_fee()
        elif choice == 5:
            add_student()  
        elif choice == 6:
            conn.close()
            break
