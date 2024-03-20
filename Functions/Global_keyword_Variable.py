

a=10

def deposit():
    global a
# global keyword is used to print global varibale value as local varivale value.
    a=100
    print("Inside deposit", a)

deposit()
print("outside deposit ",a)

# To access and modify Global varibale value inside function when both local and global variable is same.

x=90
print("id of global x",id(x))
def withdraw():
    x=80
    print("id of local x ",id(x))
    print("Inside withdraw function ",x)
    y=globals()['x']
    print("id of global y ",id(y))
    z=globals()['x']=99
    print("changing Global varibale value",z)
    print("Inside withdraw function ", x)

withdraw()
print("ouside withdraw function",x)