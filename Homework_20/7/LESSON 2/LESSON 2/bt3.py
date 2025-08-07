# Bài 3: Tìm trung vị (median)
# Viết hàm tinh_median(ds) nhận danh sách số nguyên và trả về trung vị (median)

'''
Khái niệm trung vị (median)
- Trung vị là giá trị ở giữa của một danh sách 
đã được sắp xếp theo thứ tự tăng dần.
- Có 2 trường hợp:
    + Nếu số lượng phần tử là lẻ 
        -> median là số ở chính giữa.
    + Nếu số lượng phần tử là chẵn 
        -> median là trung bình cộng của 2 số ở giữa.
'''

def tinh_median(ds):
    if len(ds) == 0:
        return None # Danh sách rỗng thì không có trung vị
    
    ds_sap_xep = sorted(ds) # Sắp xếp danh sách tăng dần
    n = len(ds_sap_xep)
    giua = n // 2
    
    if n % 2 == 1:
        # Nếu lượng phần tử lẻ -> lấy phần tử ở giữa
        return ds_sap_xep[giua]
    
    else:
        # Nếu lượng phần tử chẵn -> Lấy trung bình 2 phần tử giữa
        return (ds_sap_xep[giua - 1] + ds_sap_xep[giua]) / 2

print(tinh_median([1, 5, 3]))
# 1, 3, 5 -> median = 3
print(tinh_median([10, 2, 8, 4]))
# 2, 4, 8, 10 -> median = (4 + 8) / 2 = 6.0
print(tinh_median([]))
# None
    