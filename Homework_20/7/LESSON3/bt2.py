# Bài 2: Tạo lớp Car
# Yêu cầu: Viết lớp Car có các thuộc tính brand, color và speed. 
# Viết phương thức display_info() để in thông tin của xe.
class Car:
    def __init__(self, brand, color, speed):
        self.brand = brand    
        self.color = color    
        self.speed = speed    

    def display_info(self):
        print("Thông tin xe:")
        print("Hãng:", self.brand)
        print("Màu:", self.color)
        print("Tốc độ:", self.speed, "km/h")


my_car = Car("Toyota", "Đỏ", 120)

my_car.display_info()

        
        