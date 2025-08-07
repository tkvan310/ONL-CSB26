class Car :
    def __init__(self, color, mileage):
        self.color = color   
        self.mileage = mileage
        
    def mo_ta(self):
        print(f"Chiếc xe có màu {self.color} và chạy được {self.mileage} km")
        
xe1 = Car("đỏ", 20 )
xe2 = Car("xanh",50 )
xe1.mo_ta()
xe2.mo_ta()
        
        