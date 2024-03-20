# In Python, method overloading isn't directly supported as it is in some other languages like Java or C++.
# However, you can achieve similar functionality using default parameter values and variable-length argument lists.
class Calculation:

    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    def sum(self, a=None, b=None, c=None):

        if a != None and b != None and c != None:
            sum = a + b + c
        elif a != None and b != None:
            sum = a + b
        else:
            sum = a
        return sum
c1=Calculation(100,200)
print(c1.sum(10,20,30))
print(c1.sum(12,22))
print(c1.sum(34))

