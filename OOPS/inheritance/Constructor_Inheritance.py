class A:
    def __init__(self):
        print("in A init")

    def feature1(self):
        print("Feature 1 working")

    def feature2(self):
        print("Feature 2 working")


class B(A):
    def __init__(self):
        super().__init__()
        print("in B init")

    def feature3(self):
        print("Feature 3 working")

    def feature4(self):
        print("Feature 4 working")

a1=A()
a1.feature2()

b1=B()
b1.feature1()

a1=B()
a1.feature2()
a1.feature4()

# here B class has init means constructor so it wont call super class init. if it not found it will call
#class A init . To test comment the class B init
#If we want to call the init method of super class use super().__init__()

