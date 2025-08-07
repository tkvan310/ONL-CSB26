# Bài 7: Tính mean, median, mode từ file
# Đọc file data.txt chứa danh sách số, sau đó gọi các hàm đã viết ở bài 2–4 để tính và in kết quả.

def tinh_mean(ds):
    if len(ds) == 0:
        return 0 # Tránh chia cho 0
    return sum(ds) / len(ds)

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
    max_lan_xuat_hien = max(dem.values())
    
    # # Trả về phần tử đầu tiên có tần suất lớn nhất
    # for so, so_lan in dem.items():
    #     if so_lan == max_lan_xuat_hien:
    #         return so
    
    # Lọc tất cả phần tử có số lần xuất hiện bằng max
    modes = [so for so, sl in dem.items() if sl == max_lan_xuat_hien]
    return modes

# Đọc số từ file và chuyển thành danh sách số nguyên
with open("Lesson2/basic/data/bt5_data.txt", "r") as f:
    ds_str = f.read().strip().split()

ds_so = [int(so) for so in ds_str]

# Gọi các hàm thống kê
mean = tinh_mean(ds_so)
median = tinh_median(ds_so)
mode = tinh_mode(ds_so)

# In kết quả
print("Kết quả thống kê từ file data.txt:")
print(f"Mean: {mean}")
print(f"Median: {median}")
print(f"Mode: {mode}")    
    