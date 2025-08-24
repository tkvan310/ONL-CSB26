# Hệ thống quản lí tài khoản ngân hàng
#BankAccount
class BankAccount():
     def __init__(self, account_number, owner,__balance):
         self.account_number = account_number
         self.owner = owner
         self.balance = __balance
     def deposit(self, amount):
         if amount > 0:
             self.balance += amount
             print(f"Nạp{amount} VNĐ vào số tài khoản{self.account_number} thành công")
         else:
             print("[!] Số tiền không hợp lệ")
     def display_info(self):
        print(" Thông tin tài khoản: ")
        print(f" Số tài khoản : {self.account_number}")
        print(f" Tên tài khoản : {self.owner}")
        print(f" Số dư tài khoản :{self.balance} VNĐ")
# Tài khoản chính
class CheckingAccount(BankAccount):
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"[-] Đã rút {amount} VNĐ từ tài khoản {self.account_number}.")
        else:
            print("[!] Không đủ số dư để rút.")
# Tài khoản tiết kiệm
class SavingAccount(BankAccount):
    def __init__(self, account_number, owner, balance=0, interest_rate=0.05, locked=True):
        super().__init__(account_number, owner, balance)
        self.interest_rate = interest_rate
        self.locked = locked  # True: chưa đến kỳ rút

    def apply_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        print(f"[+] Đã cộng lãi {interest:.0f} VNĐ vào tài khoản tiết kiệm.")

    def withdraw(self, amount):
        if self.locked:
            print("[!] Không thể rút: Tài khoản đang bị khóa (chưa đến kỳ).")
        elif amount <= self.balance:
            self.balance -= amount
            print(f"[-] Đã rút {amount} VNĐ từ tài khoản tiết kiệm.")
        else:
            print("[!] Số tiền rút vượt quá số dư.")    
        
print("===== TÀI KHOẢN CHÍNH =====")
tk_chinh = CheckingAccount("001", "Thiều Khánh Vân", 500000)
tk_chinh.display_info()
tk_chinh.deposit(200000)
tk_chinh.withdraw(100000)
tk_chinh.display_info()
    
    
                 
    
    
         
         
         
         