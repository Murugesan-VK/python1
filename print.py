# Printing a simple string
print("Hello, world!")

# Printing variables
name = "Alice"
age = 30
print("Name:", name)
print("Age:", age)

# Printing multiple items separated by a space (default behavior)
print("Name:", name, "Age:", age)

# Printing with formatted strings (f-strings)
print(f"Name: {name}, Age: {age}")

# Printing with format() method
print("Name: {}, Age: {}".format(name, age))

# Printing with different separators
print("Python", "is", "awesome", sep="-")
print("Python", "is", "awesome", sep="*")

# Printing with end parameter to change the end character
print("Hello,", end=" ")
print("world!")

# Printing without a newline character
print("This is on", end=" ")
print("the same line.")

print("-----------------------------------------------------------------------")
# Prompting the user for different types of input
name = input("Enter your name: ")  # string input
age = int(input("Enter your age: "))  # integer input
height = float(input("Enter your height (in meters): "))  # float input
is_student = input("Are you a student? (True/False): ").lower()  # boolean input

# Converting string input to boolean
is_student = is_student == 'true'

# Printing the input values along with their data types
print("Name:", name, type(name))
print("Age:", age, type(age))
print("Height:", height, type(height))
print("Is Student:", is_student, type(is_student))

print("-----------------------------------------------------------------------")
