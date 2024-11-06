#Error handling => Handle the error
#compile time Error => syntax mistake

print("Hi")
print("Bye")
print("Hey")
#NameError:
#Logical error => Do not show Error
a=10
b=10
print("a+b:",a+a) #logical error
print("      --- ")
#Runtime error => User mistake 
a=int(input())
b=int(input())
print(a+b)
#ValueError:
print("--------------------------------------------------------------------")
#Exception Handling
try:
    a=int(input(""))
    b=int(input())
    print(a+b)
except Exception:
    print("Error Bro")
print("--------------------------------------------------------------------")
try:
    a=int(input("Enter A:"))
    b=int(input("Enter B:"))
    print(a+b)
except Exception as e:
    print("Error Bro",e)
print("--------------------------------------------------------------------")
try:
    a=input()
    b=input()
    print(a+b)
except Exception as e:
    print("Error Bro",e)
print("--------------------------------------------------------------------")
try:
    a=input()
    b=input()
    print(a/b)
except Exception as e:
    print("Error Bro",e)
print("--------------------------------------------------------------------")
try:
    a=int(input())
    b=int(input())
    c=input()
   # print(c/a)
    print(d)
except ValueError as e:
    print("Value Error:",e)
except TypeError as e: #step2
    print("Type Error:",e)
except Exception:
    print("Wrong")
finally:
    print("Done")
print("---------------------------------------------------------------------")


















