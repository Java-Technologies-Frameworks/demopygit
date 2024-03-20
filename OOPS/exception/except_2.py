try:
    # Code that may raise exceptions
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    result = num1 / num2
    print("Result:", result)
except ValueError:
    # Handling ValueError if the user enters non-numeric input
    print("Please enter valid numeric inputs.")
except ZeroDivisionError:
    # Handling ZeroDivisionError if the user enters 0 as the second number
    print("Cannot divide by zero!")
except Exception as e:
    # Handling any other type of exception
    print("An error occurred:", e)
else:
    # Executed if the try block does not raise an exception
    print("Division successful!")
finally:
    # Cleanup code that always executes, regardless of exceptions
    print("Execution complete.")