# Bài 22: Đếm số lớn hơn trung bình
# Viết chương trình nhập danh sách số, tính trung bình, sau đó đếm có bao nhiêu số lớn hơn giá trị đó.

def dem_lon_hon_trung_binh(ds):
    if len(ds) == 0:
        return 0

    trung_binh = sum(ds) / len(ds)
    dem = 0
    for so in ds:
        if so > trung_binh:
            dem += 1
    return dem

danh_sach = [float(x) for x in input("Nhập các số, cách nhau bởi dấu cách: ").split()]
ket_qua = dem_lon_hon_trung_binh(danh_sach)
print("Số lượng phần tử lớn hơn trung bình là:", ket_qua)
