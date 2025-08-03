# Bài 1: Nhập danh sách số từ người dùng
# Viết chương trình cho phép người dùng nhập vào một danh sách các số nguyên, kết thúc khi nhập 'x'.
# Sau đó in danh sách ra màn hình.

# Bước 1: Tạo danh sách rỗng
ds = []

# Bước 2: Dùng vòng lặp để nhập liên tục
while True :
    nhap = input("Nhập số nguyên (hoặc 'x' để giữ nguyên):")
    if nhap.lower() == 'x':
        break
    try:
       so = int(nhap)
       ds.append(so)
    except ValueError:
        print(" Vui lòng nhập số hợp lệ")
    
        
        
# Bước 3: In danh sách ra màn hình
print(" Danh sách số nguyên đã nhập",ds)

    
        
