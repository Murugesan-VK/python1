'''
def greet(name):
    return f"Hello, {name}! Welcome to Python modules."

def add(a, b):
    return a + b

PI = 3.14159

# Import the custom module
import mymodule

# Using the functions and variables from the module
name = "Sasi"
greeting = mymodule.greet(name)
print(greeting)

# Using the add function
result = mymodule.add(10, 20)
print(f"10 + 20 = {result}")

# Using the variable PI
print(f"Value of PI: {mymodule.PI}")
'''
import variables

fact_of_6 = variables.factorial(6)

power_of_6 = variables.power[6]

alphabet_2 = variables.alphabets[1]

print(f"The factorial of 6 is: {fact_of_6}")
print(f"Power of 6 is: {power_of_6}")
print(f"Second Alphabet is: {alphabet_2}")
