# Bài 13: Đảo ngược danh sách
# Viết hàm dao_nguoc(ds) trả về danh sách bị đảo ngược

def dao_nguoc(ds):
    return ds [::-1]    

danh_sach = [1,2,3,4,5,6,7,8]
ket_qua = dao_nguoc(danh_sach)
print(" Danh sách bị đảo ngược là ", ket_qua)
