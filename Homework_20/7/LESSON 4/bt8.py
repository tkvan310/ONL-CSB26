import random

def binary_search(arr, x):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            left = mid + 1
        else:
            right = mid - 1

    return -1  

danh_sach = random.sample(range(1, 101), 30)

danh_sach.sort()

print("Danh sách đã sắp xếp:")
print(danh_sach)

try:
    x = int(input("Nhập số cần tìm: "))
except ValueError:
    print("Vui lòng nhập một số nguyên.")
    exit()

vi_tri = binary_search(danh_sach, x)

if vi_tri != -1:
    print(f"Tìm thấy {x} tại vị trí {vi_tri}")
else:
    print(f"Không tìm thấy {x} trong danh sách")