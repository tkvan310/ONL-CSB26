# Bài 17: Kiểm tra có tồn tại hay không
# Viết hàm kiem_tra(x, ds) kiểm tra số x có trong danh sách ds không.

def kiem_tra(x, ds):
    if x in ds:
        return True
    else:
        return False
danh_sach = [1, 3, 5, 7, 9]

print(kiem_tra(3, danh_sach))  
print(kiem_tra(4, danh_sach))  
