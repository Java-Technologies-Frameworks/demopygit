def add (a,b):
    c =a+b
    return c

a,b =100,200
res =add(a,b)
print(add(30,50))
print(res)

#person method
def person(name,age):
    print(name)
    print(age)

person('prasanna',30)
person(34,'saeen')
person(name='Ranjita',age=25)

#if we are not passing the value it will take default value exmple
def person1(name,age=22):
    print(name)
    print(age)
person1('ramesh')  # it will print default value
person1('ramesh',23)

def sum(*b):
    c=0
    for i in b:
        c=c+i
    print(c)
sum(5,30,45,65,55,95)
