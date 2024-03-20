import sys
sys.setrecursionlimit(2000)
print(sys.getrecursionlimit())
count =0
def greet():
    global  count
    count+=1
    print("Hello" ,count)
    greet()

#greet()


def fact(n):
    if n==0:
        return 1
    return n* fact(n-1)
res = fact(5)
print(res)
