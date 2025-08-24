import random

def linear_search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1

danh_sach = random.sample(range(1, 51), 15)

print("Danh sách ngẫu nhiên là:", danh_sach)

try:
    x = int(input("Nhập số cần tìm (1 - 50): "))
except ValueError:
    print("Bạn phải nhập một số nguyên.")
    exit()

vi_tri = linear_search(danh_sach, x)

if vi_tri != -1:
    print(f"Tìm thấy {x} tại vị trí {vi_tri}")
else:
    print(f"Không tìm thấy {x} trong danh sách")
    
