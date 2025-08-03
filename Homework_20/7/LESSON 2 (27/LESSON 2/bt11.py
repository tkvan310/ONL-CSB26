# Bài 11: Đếm số lượng số lẻ
# Viết hàm dem_le(ds) nhận danh sách số nguyên và trả về số lượng phần tử là số lẻ.
def dem_le(ds):
    return len([ so for so in ds if so % 2 != 0 ])

# Trả về số lượng phần tử là số lẻ
danh_sach = [1,2,3,4,5,6,7,8,9,0]
print (" Số lượng phần tử là số lẻ trong danh sách là : ", dem_le(danh_sach))

        
    