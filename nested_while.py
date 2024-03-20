# Outer loop to print numbers from 1 to 3
i = 1
while i <= 3:
    print("Outer loop iteration:", i,end="")

    # Inner loop to print numbers from 1 to 3 within each iteration of the outer loop
    j = 1
    while j <= 3:
        print("Inner loop iteration:", j,end="")
        j += 1

    # Increment the outer loop counter
    i += 1
    print()

