# Bài 3: Viết lớp Student
# Yêu cầu: Viết lớp Student với các thuộc tính name, grade.
# Viết phương thức is_passed() trả về True nếu điểm lớn hơn 5, ngược lại là False.

class Student():
    def __init__(self, name, grade ):
        self.name = name
        self.grade = grade
    def is_passed(self):
        return self.grade > 5  

# Ví dụ sử dụng
sv1 = Student("Khánh Vân", 7)
sv2 = Student("Kiên", 4)

print(sv1.name, "đậu?", sv1.is_passed())  
print(sv2.name, "đậu?", sv2.is_passed()) 
        
        
