class A:
    def __init__(self):
        print("in A init")

    def feature1(self):
        print("Feature 1 of A working")

    def feature2(self):
        print("Feature 2 working")


class B:
    def __init__(self):
        super().__init__()
        print("in B init")

    def feature3(self):
        print("Feature 3 working")

    def feature4(self):
        print("Feature 4 working")

    def feature1(self):
        print("Feature 1 of B working")


class C(A,B):
    def __init__(self):
        super().__init__()
        print("in C init")
    def feature5(self):
        super().feature2()
        print("Feature5 working")


c1=C() # comment super().__init__ it will print only :in C init

# Here my class C inherits from A,B , when we are using super.__init__
# so it will prefer from left to right so in A init will print.It will also work same way for method also
c1.feature1() #Feature 1 of A working
c1.feature5()
