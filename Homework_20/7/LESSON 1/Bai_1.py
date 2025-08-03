# Nhap diem cac mon cua ban Lan
diem_toan = float(input("Nhập điểm môn Toán: "))
diem_van = float(input("Nhập điểm môn Văn: "))
diem_tieng_anh = float(input("Nhập điểm môn tiếng anh: "))

# Tính điểm trung bình bằng công thức: (Toán + Văn + Anh)/3
diem_trung_binh = ( diem_toan + diem_van + diem_tieng_anh) / 3

# In ra kết quả
print (" Điểm trung bình của bạn Lan là:", round(diem_trung_binh,2))
