# Số thứ nhất
a = int(input("Hãy nhập số thứ nhất: "))
# Số thứ hai
b = int(input("Hãy nhập số thứ hai (nhập khác 0): "))

# Cách 1: Nên dùng 
tong = a + b
hieu = a - b
tich = a * b
thuong = a / b

# f-string
print(f"{a} + {b} = {tong}")
print(f"{a} - {b} = {hieu}")
print(f"{a} * {b} = {tich}")
print(f"{a} / {b} = {thuong}")
# Khởi tạo biến tong để lưu tổng các số nguyên mà người dùng nhập vào
tong = 0

# Vòng lặp vô hạn để liên tục yêu cầu người dùng nhập số
while True:
    # Yêu cầu người dùng nhập vào một chuỗi (dạng text)
    nhap = input("Nhập số nguyên (Enter để kết thúc): ")

    # Nếu người dùng nhấn Enter mà không nhập gì thì thoát khỏi vòng lặp
    if nhap == "":
        break
    
    try:
        # Chuyển chuỗi vừa nhập thành số nguyên
        so = int(nhap)
        # Cộng số vừa nhập vào biến tong
        tong += so # tong = tong + so
    except ValueError:
        # Nếu người dùng nhập không phải số nguyên, in ra thông báo lỗi
        print("Vui lòng nhập một số nguyên hợp lệ!")
        
# In ra kết quả
print("Tổng các số đã nhập là:", tong)


