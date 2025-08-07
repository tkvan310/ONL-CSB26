# Bài 12: Tìm max và min
# Viết chương trình nhập một danh sách số rồi in ra số lớn nhất và nhỏ nhất

# Viết chương trình nhập một danh sách số
ds = []
while True :
    nhap =  input(" Nhập một danh sách số ( hoặc nhấn 'x' để giữ nguyên): ")
    if nhap.lower() == 'x':
        break
    try:
        so = int(nhap)
        ds.append(so)
    except ValueError :
        print("Vui lòng nhập một số hợp lệ!")
# Tìm min và max
if len(ds) == 0:
    print(" Danh sách rỗng, không thể tìm ra min và max")
else:
    So_lon_nhat = max(ds)
    So_nho_nhat = min(ds)
    print(" Số lớn nhất là ", So_lon_nhat)
    print(" Sô nhỏ nhất là" , So_nho_nhat)
    
        
    
