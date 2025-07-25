# Nhập một số nguyên dương 
n = int(input(" Nhập một số nguyên dương: "))

# In ra tổng các số lẻ từ một đến n
if n <= 0 :
    print("Hãy nhập một số nguyên dương: ")
else:
    tong_cac_so_le = sum( i for i in range(1, n + 1, 2))
    print(f"Tổng các số lẻ từ 1 đến {n} là:{tong_cac_so_le}")
    
    # Check phải số nguyên tố không
    so_nguyen_to = True
    if n < 2 :
        so_nguyen_to = False
    else:
        for i in range (2, int(n ** 0.5) + 1):
            if n % i == 0:
                so_nguyen_to = False
                break
    if so_nguyen_to :
        print(f"{n} là số nguyên tố.")
    else:
        print(f"{n} không phải là số nguyên tố.")
    # In ra các ước số nguyên tố
    print(f"Các ước số nguyên tố của {n} là: ")
    for i in range (1, n + 1 ):
        if n % i == 0:
            print( i, end=' ')
        
        
        
    
