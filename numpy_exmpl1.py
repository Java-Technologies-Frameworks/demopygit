from numpy import *
arr= array([1,2,3,4,5,67.12])
print(arr.dtype)
print(arr)
for i in arr:
    print(i)

# now here dtype of all elements will be float


from numpy import *
arr= array([1,2,3,4,5,67.12],int)
print(arr.dtype)
print(arr)
for i in arr:
    print(i)