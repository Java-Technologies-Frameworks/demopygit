from functools import reduce
# def is_even(n):
#     return n%2==0
# nums =[1,22,33,43,56,78,43,91,87,26,29,59]
# evens= list(filter(is_even,nums))
# print(evens)

nums =[1,22,33,43,56,78,43,91,87,26,29,59]
evens= list(filter(lambda n :n%2==0,nums))
doubles= list(map(lambda n :n*2,evens))
print(evens)
print(doubles)

sum= reduce(lambda a,b:a+b,doubles)
print(sum)
#Map
