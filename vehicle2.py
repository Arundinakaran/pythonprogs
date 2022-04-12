class vehicle:
    color= "white"
    def __init__(self,mileage,maxSpeed):
        self.mileage=mileage
        self.maxSpeed=maxSpeed
class Bus(vehicle):
    def seating(self,capacity=50):
        self.capacity=capacity
        return self.capacity
class Bus(vehicle2):
    def seat(self,fare=100):
        
modelX=Bus(254,55)
print(Bus)
print(modelX.maxSpeed,modelX.mileage,modelX.seating())
print(modelX.color)
    