import math

# Basic Math Functions
print("Basic Math Functions:")
print("Square root of 16:", math.sqrt(16))
print("2 raised to the power of 3:", math.pow(2, 3))
print("Exponential value of 2:", math.exp(2))
print("Natural logarithm of 10:", math.log(10))
print("Ceiling of 3.14:", math.ceil(3.14))
print("Floor of 3.14:", math.floor(3.14))
print("Factorial of 5:", math.factorial(5))              

print("-------------------------------------------------------------------")

total = sum([1,2,2])  
print(total)   
total2 = sum([1, 2, 2],10)  
print(total2)  

print("-------------------------------------------------------------------")

#Build in function - Recursion Function
def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)
num=int(input("Enter the Number:"))
print("Factorial of",num,"is",factorial(num))

print("------------------------------------------------------------------")















        
