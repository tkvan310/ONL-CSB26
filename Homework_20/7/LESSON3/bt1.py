# Bài 1: Tạo một lớp đơn giản
# Yêu cầu: Tạo lớp Dog với các thuộc tính name và age. Viết phương thức bark() in ra “Woof! Woof!

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def bark(self):
        print("Woof! Woof!")

my_dog = Dog("Buddy", 3)
print("Chú của tôi tên là",my_dog.name)
print("Tuổi của nó là", my_dog.age)
my_dog.bark()
        
        