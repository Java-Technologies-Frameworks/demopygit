
class Car:
    # its class level java static variable
    wheels =4
    def __init__(self):
        self.mileage =20
        self.company ='BMW'

c1=Car()
c1.mileage=34
c2=Car()
Car.wheels=5
print(c1.mileage,c1.company,c1.wheels)
print(c2.mileage,c2.company,c2.wheels)




