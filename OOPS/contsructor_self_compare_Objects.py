# class Person:
#    pass
# person1=Person()
# person2=Person()
# print(id(person1))
# print(id(person2))

class Person:

    def __init__(self):
        self.name='Prasanna'
        self.age=28

    def update(self):
        self.name='saeen'
        self.age=10
    def compare(self,other):
        if self.age==other.age and self.name==other.name:
            return True
        else:
            return False




person1 =Person()
person2=Person()
person2.name='John'

# it compare the address so it will return false
if person1==person2:
    print("Both are same object")
if person1.compare(person2):
    print("Both objects are same")
else:
    print("Both are not same oBject")

print(person1.name)
print(person2.name)

person1.update()
print(person1.name,person1.age)



