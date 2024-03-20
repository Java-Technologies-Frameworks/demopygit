
try:
    a=5
    b=0
    print(a/b)
except Exception as e:
    print("Hey, we can't divide a number by zero", e)
    print("Bye")
finally:
    print("Resource closed")
