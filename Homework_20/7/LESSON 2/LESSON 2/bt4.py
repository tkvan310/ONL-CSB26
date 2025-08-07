# Bài 4: Tìm yếu vị (mode)
# Viết hàm tinh_mode(ds) trả về phần tử xuất hiện nhiều nhất trong danh sách.



'''
Khái niệm yếu vị (mode):
- Mode là giá trị xuất hiện nhiều lần nhất trong danh sách.
- Danh sách có thể có:
    + 1 mode.
    + nhiều mode.
    + hoặc không có mode rõ ràng (mỗi giá trị xuất hiện đúng 1 lần)
'''

def tinh_mode(ds):
    if len(ds) == 0:
        return [] # Không có dữ liệu
    
    dem = {} # Tạo dict để đếm số lần xuất hiện
    
    for so in ds:
        if so in dem:
            dem[so] += 1
        else:
            dem[so] = 1
    
    # Tìm phần tử có số lần xuất hiện lớn nhất
    print(dem.values())
    max_lan_xuat_hien = max(dem.values())
    
    # # Trả về phần tử đầu tiên có tần suất lớn nhất
    # for so, so_lan in dem.items():
    #     if so_lan == max_lan_xuat_hien:
    #         return so
    
    # Lọc tất cả phần tử có số lần xuất hiện bằng max
    modes = [so for so, sl in dem.items() if sl == max_lan_xuat_hien]
    return modes

print(tinh_mode([1, 2, 2, 3, 3, 3, 4])) # mode = 3
print(tinh_mode([7, 7, 1, 2, 2, 2, 7, 3])) # mode = 7
print(tinh_mode([])) # None
        
    