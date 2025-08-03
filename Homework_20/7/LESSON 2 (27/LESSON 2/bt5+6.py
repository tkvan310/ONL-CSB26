# Bài 5: Ghi danh sách vào file
# Cho một danh sách numbers = [2, 4, 6, 8]. 
# Ghi các số này vào file data.txt, mỗi số cách nhau bằng dấu cách.

numbers = [2, 4, 6, 8]

with open("data.txt","w") as file:
    content = ' '.join(str(so) for so in numbers)
    file.write(content)
    
    
# Bài 6: Đọc số từ file
# Đọc danh sách số từ file data.txt, tách các số và lưu vào danh sách kiểu int, sau đó in ra
with open ("data.txt","r") as file:
    content = file.read()
    
numbers = [int(num)for num in content.split()]
print(numbers)
    