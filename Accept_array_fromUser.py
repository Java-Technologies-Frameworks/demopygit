from array import *

arr = array('i',[])
vals=int(input("Enter the length of array"))
for i in range(vals):
    x= int(input("Enter the next value"))
    arr.append(x)
print(arr)

searchVal =int(input("Enter the value to search"))
k=0
for i in arr:
    if searchVal== i:
        print(k)
        break
    k+=1


print(arr.index(22))
