# Bài 16: Đếm tần suất xuất hiện
# Viết hàm nhận vào danh sách số và in ra tần suất xuất hiện của từng số.

def dem_tan_suat(ds):
    dem = {}  

    for so in ds:
        if so in dem:
            dem[so] += 1  
        else:
            dem[so] = 1   
            
    for so, so_lan in dem.items():
        print(f"Số {so} xuất hiện {so_lan} lần")


danh_sach = [2, 3, 2, 4, 3, 2, 5, 4]
dem_tan_suat(danh_sach)

    

