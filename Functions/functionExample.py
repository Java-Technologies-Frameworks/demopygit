def greet():
    print("hello good morning")

# calling a function
greet()

def addition():
    x =13
    b=90
    res= x+b
    print(res)
    return res

addition()

def add_fun(x,y):
    res=x+y
    print(res)

add_fun(5,11)

def add_fun1(x,y):
    res=x+y
    return res

result =add_fun1(5,11)
print("returned result :: "+str(result))

def add_sub(x,y):
    c=x+y
    d =x-y
    return c,d
result1,result2 =add_sub(10,50)
print(result1,result2)