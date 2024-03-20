class Students:
    def __init__(self, name, age, total_marks=None, address=None, mobile_number=None):
        self.name = name
        self.age = age
        self.total_marks = total_marks
        self.address = address
        self.mobile_number = mobile_number

# Create instances of the Student class with different parameters
student1 = Students("John", 20)  # Only name and age provided
student2 = Students("Alice", 22, 90, "123 Main St", "123-456-7890")  # All fields provided

# Print information about each student
print("Student 1:")
print("Name:", student1.name)
print("Age:", student1.age)
print("Total Marks:", student1.total_marks)
print("Address:", student1.address)
print("Mobile Number:", student1.mobile_number)
print()

print("Student 2:")
print("Name:", student2.name)
print("Age:", student2.age)
print("Total Marks:", student2.total_marks)
print("Address:", student2.address)
print("Mobile Number:", student2.mobile_number)
