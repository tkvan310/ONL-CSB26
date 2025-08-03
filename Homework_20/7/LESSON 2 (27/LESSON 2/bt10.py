# Bài 10: Gộp dữ liệu từ 2 file
# Đọc dữ liệu số từ hai file file1.txt và file2.txt, gộp thành một danh sách duy nhất rồi ghi vào merged.txt

def doc_file(filename):
    with open(filename, 'r') as f:
        noi_dung = f.read()
        return [int(x) for x in noi_dung.split()]

def ghi_file(filename, data):
    with open(filename, 'w') as f:
        f.write(' '.join(str(x) for x in data))

# Đọc dữ liệu từ hai file
ds1 = doc_file("file1.txt")
ds2 = doc_file("file2.txt")

# Gộp lại
ds_gop = ds1 + ds2

ghi_file("merged.txt", ds_gop)
print("Đã gộp dữ liệu và lưu vào merged.txt")
