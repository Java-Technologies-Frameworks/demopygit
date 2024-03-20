from array import *

vals=array('u',['q','a','e','i','o','x'])

newArray = array(vals.typecode,(a for a in vals))
for e in newArray:
    print(e)

# we can use while loop also here
print("new logic ")
i=0
while i<len(newArray):
    print(newArray[i])
    i+=1