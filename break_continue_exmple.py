
# arg =int(input("Enter the given number to find the prime number ::"))
# print("ind the prime number from 1 to "+str(arg))
def is_prime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

# Example usage
number = int(input("Enter a number: "))
if is_prime(number):
    print(number, "is a prime number")
else:
    print(number, "is not a prime number")


i = 1
while i <= 10:
    print(i)
    if i == 5:
        break  # Exit the loop if i reaches 5
    i += 1


print("continue example")
for j in range(1, 11):
    if j % 2 == 0:
     continue  # Skip even numbers
    print(j)


print("pass example")

for m in range(1,100):
    if(m%2!=0):
         pass
    else:
        print("m val :: "+str(m))

