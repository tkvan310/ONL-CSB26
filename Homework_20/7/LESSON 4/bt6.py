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

arr = [2, 4, 6, 8, 10, 12, 14, 16]
x = 10

result = binary_search(arr, x)

if result != -1:
    print(f"Tìm thấy {x} tại vị trí {result}")
else:
    print("Không tìm thấy")