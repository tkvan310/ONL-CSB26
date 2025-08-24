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

diem_thi = [2.5, 4.0, 5.5, 6.0, 6.5, 7.0, 8.0, 9.5]

try:
    x = float(input("Nhập điểm cần kiểm tra: "))
except ValueError:
    print("Vui lòng nhập một số hợp lệ.")
    exit()

ket_qua = binary_search(diem_thi, x)

if ket_qua != -1:
    print(f"Học sinh đạt {x} tại vị trí {ket_qua}")
else:
    print("Không có học sinh nào đạt điểm này.")