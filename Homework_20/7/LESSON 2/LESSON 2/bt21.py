# Bài 21: Tính tổng các số chẵn
# Viết hàm tong_chan(ds) trả về tổng các số chẵn trong danh sách.

def tong_chan(ds):
    tong = 0
    for so in ds:
        if so % 2 == 0:
            tong += so
    return tong

danh_sach = [1, 2, 3, 4, 5, 6]
ket_qua = tong_chan(danh_sach)
print("Tổng các số chẵn là:", ket_qua)

