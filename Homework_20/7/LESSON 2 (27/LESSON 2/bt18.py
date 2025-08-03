# Bài 18: Xoá số trùng nhau
# Viết chương trình loại bỏ tất cả các số trùng lặp trong danh sách

def xoa_trung(ds):
    ket_qua = []
    for so in ds:
        if so not in ket_qua:
            ket_qua.append(so)
    return ket_qua

danh_sach = [1, 2, 2, 3, 4, 4, 5]
print(xoa_trung(danh_sach))
