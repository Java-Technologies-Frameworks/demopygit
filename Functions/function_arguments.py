def update(x):
    print(id(x))
    x=8
    print(id(x))
    print(x)

a=10
print(id(a))
update(10)
print(a)

# here after chnaging the value of x one new address will be created as int is of immutable.
print("list check ................")
def updatelist(lst):
    print("id values of list inside update method " + str(id(lst)))
    lst[1]=10
    print("id values of list inside update method " + str(id(lst)))
    print(lst)

lst =[23,44,10,40,45,66]
print("id values of list "+str(id(lst)))
updatelist(lst)
print("lst",lst)