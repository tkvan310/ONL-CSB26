import time

# Linear Search
def linear_search(arr, num):
    for i in range(len(arr)):
        if arr[i] == num:
            return i
    return -1

# Binary Search (cần mảng đã sắp xếp)
def binary_search(arr, num):
    arr.sort()  # sắp xếp mảng
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == num:
            return mid
        elif arr[mid] < num:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# Compare Search
def compare_search(arr, num):
    # Linear Search
    start_linear = time.time()
    result_linear = linear_search(arr, num)
    end_linear = time.time()
    time_linear = end_linear - start_linear

    # Binary Search
    start_binary = time.time()
    result_binary = binary_search(arr.copy(), num)  # copy để giữ nguyên mảng gốc
    end_binary = time.time()
    time_binary = end_binary - start_binary

    # In kết quả
    print(f"Linear Search:  vị trí {result_linear}, thời gian {time_linear:.8f} giây")
    print(f"Binary Search:  vị trí {result_binary}, thời gian {time_binary:.8f} giây")

    # So sánh nhanh/chậm
    if time_linear < time_binary:
        print("➡ Linear Search nhanh hơn")
    elif time_binary < time_linear:
        print("➡ Binary Search nhanh hơn")
    else:
        print("➡ Hai thuật toán chạy gần bằng nhau")

    