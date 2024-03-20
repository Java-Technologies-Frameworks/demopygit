class Student:
    school = 'Utkal'

    def __init__(self, m1, m2, m3):
        # constructor and instance varibales
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def average(self):
        # this is a instance method we are calling on top of Object
        return (self.m1 + self.m2 + self.m3) / 3

    def getM1(self):
        # This is a accessor method to just get the values
        return self.m1

    def updateM1(self, value):
        # This is a mutator method /setter method to update m1 values
        self.m1 = value

    @classmethod
    def getSchool(cls):
        return cls.school

    @staticmethod
    def getInfo():
        print("This is a student class ::")


s1 = Student(12, 15, 20)
s2 = Student(89, 32, 90)
print(s1.average())
print(s2.average())

print(Student.getSchool())
print(Student.getInfo())
