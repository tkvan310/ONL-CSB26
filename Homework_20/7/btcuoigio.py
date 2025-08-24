class student:
    def __init__(self, name, class_name):
        self.name = name 
        self.class_name = class_name
        self.grades = []

    def add_grades(self, grade):
        self.grades.append(grade)
        
    def calculate_average(self):
        if not self.grades:
            return 0 
        return sum(self.grades) / len(self.grades)
    
    
class GradeManagement:
    def __init__(self):
        self.students = {}

    def add_students(self, name, class_name):
        if name not in self.students:
            self.students[name] = student(name, class_name)
        else:
            print(f"Học sinh '{name}' đã có mặt trong lớp.")

    def record_grade(self, name, grade):
        if name in self.students:
            self.students[name].add_grades(grade)
        else:
            print(f"Học sinh '{name}' không có tên trong danh sách. "
                  f"Hãy thêm tên vào danh sách trước tiên.")

    def calculate_average(self, name):
        if name in self.students:
            return self.students[name].calculate_average()
        else:
            print(f"Học sinh tên '{name}' không tìm thấy trong danh sách.")
            return None

    def save_data(self, filename):
        with open(filename, 'w', encoding="utf-8") as f:
            for s in self.students.values():
                Grade_str = ",".join(str(g) for g in s.grades)
                avg = s.calculate_average()
                f.write(f"Học sinh: {s.name} | Lớp: {s.class_name} | Điểm: [{Grade_str}] | Trung bình: {avg:.2f}\n")
        print(f"Dữ liệu được lưu vào {filename}")  


# Menu
def menu():
    print("\n1. Thêm một học sinh mới. ")
    print("2. Thêm điểm cho học sinh.")
    print("3. Tính điểm trung bình của một học sinh.")
    print("4. Lưu dữ liệu ra file.")
    print("5. Thoát")


gm = GradeManagement()
gm.add_students("Thiều Khánh Vân", "12A4") 
gm.record_grade("Thiều Khánh Vân","Toán", 9) 
gm.record_grade("Thiều Khánh Vân","Văn", 10) 
gm.calculate_average("Thiều Khánh Vân")

gm.save_data("students.filename")
while True:
    menu()
    choice = input("Chọn chức năng (1-5): ")
    if choice == '1':
        name = input("Nhập tên học sinh: ")
        class_name = input("Nhập tên lớp: ")
        gm.add_students(name, class_name)
    elif choice == '2':
        name = input("Nhập tên học sinh: ")
        try:
            grade = float(input("Nhập điểm: "))
            gm.record_grade(name, grade)
        except ValueError:
            print("Điểm phải là số!")
    elif choice == '3':
        name = input("Nhập tên học sinh: ")
        avg = gm.calculate_average(name)
        if avg is not None:
            print(f"Điểm trung bình của {name}: {avg:.2f}")
    elif choice == '4':
        gm.save_data("students.txt")
    elif choice == '5':
        print("Thoát chương trình.")
        break
    else:
        print("Lựa chọn không hợp lệ.")

        
        
         
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    