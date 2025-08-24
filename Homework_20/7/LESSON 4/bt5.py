import random
import time

def linear_search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1

# Hàm đo thời gian tìm kiếm
def measure_time(arr, x):
    start = time.time()
    linear_search(arr, x)
    end = time.time()
    return end - start

arr_100 = random.sample(range(1, 100000), 100)
arr_10000 = random.sample(range(1, 1000000), 10000)

x_100 = arr_100[-1]
x_10000 = arr_10000[-1]

time_100 = measure_time(arr_100, x_100)
time_10000 = measure_time(arr_10000, x_10000)

print(f"Thời gian tìm kiếm trong mảng 100 phần tử:    {time_100:.8f} giây")
print(f"Thời gian tìm kiếm trong mảng 10,000 phần tử: {time_10000:.8f} giây")

if time_100 < time_10000:
    print(" Tìm kiếm trong mảng nhỏ nhanh hơn rõ rệt.")
else:
    print(" Thời gian chênh lệch không đáng kể (có thể do máy chạy nhanh).")