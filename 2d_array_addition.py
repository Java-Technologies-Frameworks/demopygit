from numpy import *

arr1 =array([1,2,3,4,5])
arr2= array([6,1,9,3,2])
arr3 =arr1+arr2
print(sin(arr1))
print(cos(arr2))
print(log(arr3))
# this is called vectorized opereation
print(sum(arr1))
print(max(arr1))
print(concatenate((arr1,arr2)))

#IN shallow copy if we chnage some elements then it will reflect in another
arrayxy=array([2,6,8,1,3])
#shallow copy
arraymn=arrayxy
arraymn[1]=980
print(id(arrayxy))
print(id(arraymn))
print(arrayxy)
print(arraymn)

arr10=array([12,1,3,4,22,66,545,35])
arr11 =arr10.view()
#address is different but value chnage in one array reflevcts in another
print(id(arr10))
print(id(arr11))
arr10[1]=-100

print(arr10)
print(arr11)


arr99=array([12,1,3,4,22,66,545,35])
arr100 =arr99.copy()
print(id(arr99))
print(id(arr100))
arr99[1]=-200
#deep copy address of both array is diff and only arr99 1st element modofied not second.

print(arr99)
print(arr100)