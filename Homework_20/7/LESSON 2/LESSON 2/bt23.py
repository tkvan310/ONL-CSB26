# Bài 23: Chuyển chuỗi thành danh sách
# Cho chuỗi "4 6 7 9", tách các số và chuyển thành danh sách số nguyên.

chuoi = "4 6 7 9"
danh_sach_so = [ int(so) for so in chuoi.split()]
print(danh_sach_so)