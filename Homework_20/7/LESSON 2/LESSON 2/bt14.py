# Bài 14: Ghi danh sách do người dùng nhập
# Người dùng nhập từng số, ghi vào file so_nhap.txt. Kết thúc bằng nhập 'x'.

# Tạo danh sách để người dùng nhập từng số và kết thưc bằng cách nhập 'x'
with open("so_nhap.txt",'w') as f:
 while True :
    nhap = input(" Nhấp số ngẫu nhiên ( hoặc kết thúc bằng cách nhập 'x'):")
    if nhap.lower() == 'x':
        break
    try:
        so = int(nhap)
        f.write(str(so) + '\n')
    except ValueError :
        print("Vui lòng nhập số hợp lệ")
        
with open("so_nhap.txt") as file:
    content = file.read()
numbers = [ int (num) for num in content.split()]
print (numbers)

