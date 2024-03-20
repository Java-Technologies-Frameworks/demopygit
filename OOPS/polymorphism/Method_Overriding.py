class A:
    def show(self):
        print("A in show")

class B(A):
    def show(self):
        print("B in Show")

a1=A()
a1.show()
b1=B()
b1.show()
a2=B()
a2.show()
b2=A()
b2.show()
b1=b2

# in Python its allowed to store parent Object in child reference
