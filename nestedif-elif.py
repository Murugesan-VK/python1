'''
mark=int(input("Enter the Mark:"))
if mark>35:
    print("Pass")
else:
    print("Fail")
print("|------------------------------------------------|")
income=int(input("Enter Income:"))
if income>7000:
    print("Not Eligible for Scholarship")
else:
    print("Income is Greater than 7000")
print("|------------------------------------------------|")
income=int(input("Enter the Number:"))
if income%2==0:
    print("Even Number")
else:
    print("Odd Number")
print("|------------------------------------------------|")
value=int(input("Enter the Number:"))
if value%5==0 and value%3==0:
    print("It is Divisible by 3 and 5")
else:
    print("It is Not Divisible by 3 and 5")
print("|------------------------------------------------|")
score=int(input("Enter the Score Out of 100:"))
if score<35:
    print("Poor Student")
elif score=>35 and score<=70:
    print("Average Student")
elif score>70 and score<=100:
    print("Good Student")
else:
    print("Invalid Score")
print("|------------------------------------------------|")
a=int(input("Enter the First Number:"))
b=int(input("Enter the Second Number:"))
choice=input("Mini Calculator\nadd/sub/mul/div\nEnter your choice:")
if choice=="add":
    print("Your Option is Addition")
    print("Addition is:",a+b)
elif choice=="sub":
    print("Your Option is Subtraction")
    print("Subtraction is:",a-b)
elif choice=="mul":
    print("Your Option is Multiplication\n")
    print("Multiplication is:",a*b)
elif choice=="div":
    print("Your Option is Division\n")
    print("Division is:",a/b)
else:
    print("Invalid Choice")
print("|------------------------------------------------|")
score=int(input("Enter the Score Percentage:"))
if(score>70):
    name=input("Enter Your Name:")
    department=input("Enter Department Name and Location:")
    print("You Are Eligible")
else:
    print("You Are Not Eligible")
print("|------------------------------------------------|")
salary=int(input("Enter Salary:"))
age=int(input("Enter Age:"))
if salary>=20000 or age<=25:
    loan=int(input("Enter Loan Amount:"))
    if loan<=50000:
        print("You Are Eligible For Loan")
    elif loan>50000:
        print("Maximum Loan Amount is 50000")
else:
    print("You Are Not Eligible For Loan")
print("|------------------------------------------------|")'''
'''
eng=int(input("Enter English Mark:"))
tam=int(input("Enter Tamil Mark:"))
mat=int(input("Enter Maths Mark:"))
sci=int(input("Enter Science Mark:"))
soc=int(input("Enter Social Mark:"))
tot=eng+tam+mat+sci+soc
avg=tot/5
print("Enter Total Mark:",tot)
print("Enter Avg Mark:",avg)
if avg<=35:
    print("Additional Class Required")
else:
    print("You Are Good to go")
'''
print("1.Login \n2.Logout")
a=int(input("Enter Your Choices:"))
if a==1:
    b=input("User Name:")
    c=input("Create Password:")
    d=input("Re-enter Your Password for Confirmation:")
    if d==c:
        print("Password Create Succesfully")
    else:
        print("Wrong Password")
elif a==2:
    e=input("User name:")
    f=input("password")
    g=input("Re-enter Your Password")
    if g==f:
        print("User Login Out")
else:
    print("Invalid num")
    














