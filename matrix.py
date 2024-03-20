from numpy import *

m1=matrix('1 2 3 4 ; 5 6 7 8')
m2=matrix('1 2 3 ;4 5 6 ;7 8 9')
print(m1)
print(m2)
print(diagonal(m2))
print(m1.max())
print(m1.min())

#multiplication of 2 matricses

#no of columns in a matrix1 must be same with number of rows in matrix2
a=matrix('1 2 5;6 7 5;8 9 0;1 5 3')
b=matrix('3 1 9;8 6 4;9 7 6')
res= a*b
print(res)