# Bài 20: Lưu tên học sinh vào file
# Nhập danh sách tên học sinh và ghi vào file ten_hocsinh.txt, mỗi tên trên một dòng.

danh_sach_ten = []

print("Nhập tên học sinh (gõ 'x' để kết thúc):")
while True:
    ten = input("Nhập tên: ")
    if ten.lower() == 'x':
        break
    danh_sach_ten.append(ten)

with open("ten_hocsinh.txt", "w") as f:
    for ten in danh_sach_ten:
        f.write(ten + "\n")

print ("Đã lưu danh sách vào file ten_hocsinh.txt.")
