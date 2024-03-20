x = 10
y = 20

z = x + y
print(z)
print(int.__add__(x, y))


# print(str.__add__(x,y))

class Student:
    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    def __add__(self, other):
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2
        s3 = Student(m1, m2)
        return s3


    def __gt__(self, other):
        total_marks_self = self.m1 + self.m2
        total_marks_other = other.m1 + other.m2
        return total_marks_self > total_marks_other

    def __str__(self):
        return '{} {} '.format(self.m1,self.m2)


s1 = Student(42, 111)
s2 = Student(60, 500)
s3 = s1 + s2
print(s3.m1)
print(s3.m2)

if s1 > s2:
    print("s1 has higher total marks than s2")
else:
    print("s2 has higher total marks than s1")

a=9
print(a.__str__())
print(s1.__str__())

# need to overload operator __str__ otherwise for class type it will print address
print(s1)
print(s2)

