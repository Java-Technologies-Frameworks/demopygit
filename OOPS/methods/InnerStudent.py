class InnerStudent:

    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno
        self.lap = self.Laptop()  # Creating an object of Laptop inside InnerStudent

    def show(self):
        print(self.name,self.rollno)

    class Laptop:

        def __init__(self):
            self.brand='HP'
            self.cpu='I5'
            self.ram= 8

        def show(self):
            print(self.brand,self.cpu,self.ram)



s1=InnerStudent('Prasanna',32)
s2=InnerStudent('Ashok',26)

lap1=s1.lap
lap2=s2.lap
print(id(lap1))
print(id(lap2))
s1.show()
s1.lap.show()

laptop =InnerStudent.Laptop()
laptop.show()

#Instaed of creating Laptop class obj outside the Student class, create inside the class using Inner class
#if we are sure the Laptop class is not used anywhere except Student, so crate a
# inner class to Student in name of Laptop