'''
a=int(input("Total employees:"))
print("Enter ",a," employees name:")
list=[]
i=1
while i<=a:
    name=input("Enter the Name:")
    list.append(name)
    i=i+1
print(list)
print(type(list))
'''
'''
a=input("Available Courses \n1.AI-10000\n2.ML-12000\n3.DS-15000\n4.FrontEnd-20000\n Select your Cources:")
i=1
c=0
student_name=[]
b=int(input("Total Students:\n"))
print("Enter",b," Student Name:")
while i<=b:
    name=input("Enter Student Name:")
    student_name.append(name)
    i=i+1
while c<=b:
    print("Enter the Address for",student_name[c])
    address=input("Enter Your Address:")
    phone=input("Enter Phone Number:")
    c=c+1
'''
'''
a=int(input("Enter the number limits:"))
i=1
new_lists=[]
while i<=a:
    num=int(input())
    new_list.append(num)
    i=i+1
print(new_list)
j=0
odd=0
even=0
length=len(new_list)
while j<length:
    b=new_list[j]
    if b%2==0:
        even=even+1
    else:
        odd=odd+1
    j=j+1
print("Total Even Number:",even)
print("Total Odd Number:",odd)
'''

input_list = input("Enter a list of integers,separated by spaces: ")
my_list = [int(num) for num in input_list.split()]

even_count = 0
odd_count = 0

for num in my_list:
    
    if num % 2 == 0:
        even_count += 1
    
    else:
        odd_count += 1

print("Total even numbers:", even_count)
print("Total odd numbers:", odd_count)




















    




