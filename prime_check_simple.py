class prime_chcek:

    def primeNumberCheck(num):
        if num%2==0:
            print("Not a prime number")
        else:
            print(str(num)+"is a prime number")

num = int(input("Enter the number ::"))
print("number received from usrr is :: " + str(num))
prime_chcek.primeNumberCheck(num)