def goi_so(arr, x):
    count = 0
    for i in range(len(arr)):
        if arr[i] == x:
            count += 1
    return count

arr = [1, 2, 3, 2, 4, 2, 5]
x = int(input("Nhập phần tử cần đếm: "))

so_lan = goi_so(arr, x)
print(so_lan)