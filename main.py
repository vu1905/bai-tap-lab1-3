# main.py gốc trên nhánh main
def tinh_diem_gpa(diem_so):
    # Công thức tuyến tính đơn giản của Dev A
    if diem_so >= 8.5 : 
        return 4.0 #code cua devB
    else:
        return round((diem_so / 10) * 4, 2) #code cua deva


print("Điểm GPA hệ 4 là:", tinh_diem_gpa(8.5))
