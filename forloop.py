'''for i in "apple":
    print(i)
print("|------------------------------------------------|")
for i in range(11):
    print(i)
print("|------------------------------------------------|")
for i in range(1,5):
    print(i)
print("|------------------------------------------------|")
table=int(input("Enter the Table:"))
for i in range(1,11):
    print(table,"X",i,"=",table*i)
print("|------------------------------------------------|")
a=int(input("Enter First Number:"))
b=int(input("Enter Last Number:"))
for i in range(a+1,b):
    print(i)
print("|------------------------------------------------|")
for i in range(2,11,2):
    print(i)
print("|------------------------------------------------|")
count=0
for i in range(1,11):
    if i%2==0:
        count=count+1
print(count)
print("|------------------------------------------------|")
even=0
odd=0
for i in range(1,11):
    if i%2==0:
        even=even+1
    else:
        odd=odd+1
print("Total Even Number:",even)
print("Total Odd Number:",odd)
print("|------------------------------------------------|")
divide=0
nodivide=0
for i in range(1,101):
    if i%5==0 and i%3==0:
        divide=divide+1
    else:
        nodivide=nodivide+1
print("It Is Divisible By 3 and 5:",divide)
print("It Is Not Divisible By 3 and 5:",nodivide)
print("|------------------------------------------------|")
print("List")
print("5 Natural Number")
s=0
for i in range(1,6):
    s=s+i
print(s)
print("|------------------------------------------------|")'''
total=0
lists=[]
for i in range(1,11):
    a=int(input("Enter the Number:"+str(i) ))
    total=total+a
    lists.append(a)
print(lists)
print("total mark:",total)
avg=total/10
print("Average mark:",avg)





















