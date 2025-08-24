# Bài 4: Giấu thông tin tài khoản ngân hàng
# Yêu cầu: Viết lớp BankAccount có thuộc tính riêng __balance. 
# Viết các phương thức deposit(amount), withdraw(amount), get_balance().

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance  

    def get_balance(self):       
        return self.__balance

    def deposit(self, amount):   
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):  
        if 0 < amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Rút không hợp lệ hoặc không đủ tiền.")
            
            
            
acc = BankAccount("Vân", 1000)

print(acc.owner)        
print(acc.get_balance())   

acc.deposit(500)
acc.withdraw(200)
print(acc.get_balance())  






