'''
def function():
    print("Hello World")
function()
print("-----------------------------------------------------------------------")
def add():
    print("Addition")
    print("--------")
    a=int(input("Enter A Value:"))
    b=int(input("Enter B Value:"))
    print("Addition is:",a+b)
def sub():
    print("Subtraction")
    print("-----------")
    a=int(input("Enter A Value:"))
    b=int(input("Enter B Value:"))
    print("Subtraction is:",a-b)
def mul():
    print("Multiplication")
    print("--------------")
    a=int(input("Enter A Value:"))
    b=int(input("Enter B Value:"))
    print("Multiplication is:",a*b)
def div():
    print("Division")
    print("--------")
    a=int(input("Enter A Value:"))
    b=int(input("Enter B Value:"))
    print("Division is:",a/b)
mul()
print("-----------------------------------------------------------------------")
a=int(input("Enter A Value:"))
b=int(input("Enter B Value:"))
def add():
    print("Addition:",a+b)
def sub():
    print("Subtraction:",a-b)
def mul():
    print("Multiplication:",a*b)
def div():
    print("Division:",a/b)
add()
print("-----------------------------------------------------------------------")
def evenorodd(i):
    if i%2==0:
        print("Even Number")
    else:
        print("Odd Number")
evenorodd(int(input("Enter the Number:")))
print("-----------------------------------------------------------------------")
def passorfail(i):
    if i>35:
        print("Pass")
    else:
        print("Fail")
passorfail(int(input("Enter the Mark:")))
print("-----------------------------------------------------------------------")
def printrange(a,b):
    while a<=b:
        print(a)
        a=a+1
printrange(int(input("Enter the First Number:")),int(input("Enter the Last Number:")))
print("-----------------------------------------------------------------------")'''
'''
def printrange(a,b):    #variable 
    while a<=b:
        print(a)
        a=a+1
a=int(input("Enter the First Number:"))
b=int(input("Enter the Last Number:"))
printrange(a,b) #values
print("-----------------------------------------------------------------------")'''
'''
def ganesh():
    number = input("Enter your a/c number : ")
    name = input("Enter your name : ")
ganesh()
ganesh()
print("-----------------------------------------------------------------------")'''
'''
    #greet() -> Name of the function
def greet():  #def keyword is used to create a function
    print("Inside function")    #function body
print("Hello,World")
greet()     #call of the function
print('Outside function')
print("-----------------------------------------------------------------------")'''
'''
#With Argument (Without or No) Return
def greet(a,b,e):
    print("Welcome",a,"This is your phone number:",b)
c=input("Enter Your Name:")
d=int(input("Enter your Phone Number:"))
e=input("Enter Your Name")
greet(c,d,e)

#Without Argument With Return
def greet():
    b=int(input("Enter Your Return Code:"))
    print("Your Returning request is sent...")
    return b
print("What you Want \n1.Return \n2.Sales")
value=input("Enter Your Option:")
if(value=='1'):
    print(greet())
    
#With Argument With Return
def greet(b):
    print("Welcome,",b)
    c=int(input("Enter Your Return code:"))
    print("Your Returning request is sent...")
    return c
i=input("Enter your name:")
print("What you Want \n1.Return \n2.Sales")
value=input("Enter Your Option:")
if(value=='1'):
    print(greet(i))

#Without Argument Without Return
def greet():
    print("Inside function")
    
print('outside function')
greet()

'''
'''
a=input("Enter the Number:")
length=len(a)
print(length,"Digit")
b=10
i_str=int(a)
print(i_str+b)
'''
'''
#Arbitary  Function
def saran(*args):
    total = sum(args)
    print("Total : ",total)
    average = total / len(args)
    #print("Type of average : ",type(average))
    return average

# Calling the function with different numbers of arguments

result2 = saran(2, 4, 6, 8,10,89)
result3 = saran(1, 3, 5,8,72)

# Printing the results
print("Average 1:", result2)
#print("Average 2:", result2)
print("Average 3:", result3)
'''
'''
#Random Function
import random

# Generate a random integer between 1 and 10 (inclusive)
random_number = random.randint(1, 10)
print("Random number:", random_number)

# Generate a random floating-point number between 0 and 1
random_float = random.random()
print("Random float:", random_float)

# Generate a random element from a list
my_list = [1, 2, 3, 4, 5]
random_element = random.choice(my_list)
print("Random element:", random_element)
'''
'''
#Lamda Function
# Python code to demonstrate ananymous functions  
# Defining a function    
lambda_ = lambda argument1, argument2: argument1 + argument2;    
    
# Calling the function and passing values    
print("Value of the function is : ", lambda_(20,30))    
print("Value of the function is : ", lambda_(40,50))    
'''
#conversion Function
a=10
b=20
print(a+b)
b=float(a)
print(a+b)
a=int(b)
print(a+b)
print(b+a)
a=str(b)
print(a+a)




























