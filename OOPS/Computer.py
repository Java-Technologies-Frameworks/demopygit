
class Computer:
    def config(self):
        print("i5,16gb,1TB")
a='9'
print(type(a))
comp1=Computer()
comp2=Computer()
comp3=Computer()
print(type(comp1))

Computer.config(comp1)
Computer.config(comp2)

#Recommeneded way is 2nd one 
comp1.config()
comp2.config()