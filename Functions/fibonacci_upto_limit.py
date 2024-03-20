def fibonacci(limit):
    a = 0
    b = 1

    if limit == 0:
        print(a)
    elif limit == 1:
        print(a)
        print(b)
    else:
        print(a)
        print(b)

    # Generate Fibonacci numbers using a for loop
    for _ in range(2, limit):
        c = a + b
        if c >= limit:
            break
        a = b
        b = c
        print(c)

# Call the function with limit as 100
fibonacci(100)
