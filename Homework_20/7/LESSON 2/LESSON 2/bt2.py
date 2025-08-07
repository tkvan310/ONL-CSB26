# Bài 2: Tính trung bình (mean)
# Viết hàm tinh_mean(ds) nhận một danh sách số và trả về giá trị trung bình cộng.

# Hàm tính trung bình cộng của một danh sách
def tinh_mean(ds):
    if len(ds) == 0:
        return 0 # Tránh chia cho 0
    return sum(ds) / len(ds)

# Gọi hàm với danh sách cụ thể
danh_sach = [5, 10, 15, 20]
ket_qua = tinh_mean(danh_sach)
print("Trung bình cộng là:", ket_qua)
    
    
    