def linear_search( arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1
ds = ["An","Bình", "Chi", "Dung"]
x = input("Nhập tên học sinh cần tìm :")
vi_tri = linear_search(ds,x)

if vi_tri != 1:
    print(f"Tìm thấy tại vị trí {vi_tri}")
else:
    print(f"Không tìm thấy tại vị trí {vi_tri}")