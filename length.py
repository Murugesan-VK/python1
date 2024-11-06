#length
x = 5
y = 5

print("is Operator:")
print("x is y:", x is y)

print("\nis not Operator:")
print("x is not y:", x is not y)

#maximum and Minimum
numbers = [10, 20, 5, 8, 15]
max_num = max(numbers)
min_num = min(numbers)
print("Maximum number:", max_num)
print("Minimum number:", min_num)

#Absolute
a = -10  #negative value convert into postive value
print(abs(a))

#Round

# Conversion and Formatting with Concatenation

# String Concatenation
string6 = "Hello"
string7 = "World!"
concatenated_string = string6 + ", " + string7
print("Concatenated String:", concatenated_string)  # Output: Hello, World!

# str.capitalize()
string1 = "hello, world!"
print("capitalize():", string1.capitalize())  # Output: Hello, world!

# str.lower()
string2 = "HELLO, WORLD!"
print("lower():", string2.lower())  # Output: hello, world!

# str.upper()
string3 = "hello, world!"
print("upper():", string3.upper())  # Output: HELLO, WORLD!

# str.title()
string4 = "hello, world!"
print("title():", string4.title())  # Output: Hello, World!

# str.swapcase()
string5 = "Hello, World!"
print("swapcase():", string5.swapcase())  # Output: hELLO, wORLD!

# str.format()
name = "Alice"
age = 30
print("My name is {} and I am {} years old.".format(name, age))  # Output: My name is Alice and I am 30 years old.
