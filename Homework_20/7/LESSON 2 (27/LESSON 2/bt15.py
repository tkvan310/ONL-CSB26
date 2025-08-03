# Bài 15: Lọc số lẻ từ file
# Đọc so_nhap.txt, lọc ra các số lẻ và ghi vào so_le.txt.

with open ("so_nhap.txt",'r') as file :
    content = file.readlines()
    
so_le = []
for dong in content:
    try:
        so = int(dong.strip())  
        if so % 2 != 0:         
            so_le.append(str(so))  
    except ValueError:
        continue  

with open("so_le.txt", 'w') as  file :
    for so in so_le:
        file.write(so + "\n") 
        
