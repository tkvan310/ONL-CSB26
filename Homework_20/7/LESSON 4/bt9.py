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

arr = random.sample(range(1, 100000), 5000)

x = arr[-1]

start_linear = time.time()
result_linear = linear_search(arr, x)
end_linear = time.time()
time_linear = end_linear - start_linear

arr_sorted = sorted(arr)  # không làm thay đổi mảng gốc
start_binary = time.time()
result_binary = binary_search(arr_sorted, x)
end_binary = time.time()
time_binary = end_binary - start_binary

print(f"Linear Search:  vị trí {result_linear}, thời gian {time_linear:.8f} giây")
print(f"Binary Search:  vị trí {result_binary}, thời gian {time_binary:.8f} giây")

if time_linear > time_binary:
    print("➡ Binary Search nhanh hơn")
elif time_binary > time_linear:
    print("➡ Linear Search nhanh hơn (hiếm khi xảy ra)")
else:
    print("➡ Thời gian gần bằng nhau")