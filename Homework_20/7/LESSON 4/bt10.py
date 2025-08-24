import random
import time

def linear_search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1

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


print("Chọn phương pháp tìm kiếm:")
print("1. Linear Search (tuyến tính)")
print("2. Binary Search (nhị phân)")
choice = input("Nhập 1 hoặc 2: ")

arr = random.sample(range(1, 100000), 10000)  

try:
    x = int(input("Nhập số cần tìm: "))
except ValueError:
    print("Vui lòng nhập một số nguyên.")
    exit()

if choice == "1":
    print("\nĐang dùng Linear Search...")
    start = time.time()
    result = linear_search(arr, x)
    end = time.time()
elif choice == "2":
    print("\nĐang dùng Binary Search (sắp xếp mảng trước)...")
    arr.sort()  
    start = time.time()
    result = binary_search(arr, x)
    end = time.time()
else:
    print("Lựa chọn không hợp lệ.")
    exit()

thoi_gian_chay = end - start

if result != -1:
    print(f"Tìm thấy {x} tại vị trí {result}")
else:
    print(f"Không tìm thấy {x} trong mảng.")

print(f"Thời gian chạy: {thoi_gian_chay:.8f} giây")