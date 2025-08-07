# Bài 9: Lọc theo điều kiện
# Viết chương trình cho phép nhập một số x, sau đó lọc và in ra các số trong danh sách lớn hơn x.
def loc_so_lon_hon(ds, x):
    return [so for so in ds if so > x]

danh_sach = [3, 7, 2, 10, 5, 8]

x = int(input("Nhập số x: "))
ket_qua = loc_so_lon_hon(danh_sach, x)

# In kết quả
print("Các số lớn hơn", x, "là:", ket_qua)
