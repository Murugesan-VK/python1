while True:
    choice=input("1.createFile\n2.WriteFile\n3.readFile\n4.AppendFile\n5.Exit \n Enter your choice : ")
    if choice=="1":
        name=input("Enter Your File Name : \n")
        o=open(name,"w")
        # o.write("yes its worked\n")
        # o.close()
        break
    elif choice=='2':
        name=input("Enter Your File Name : \n")
        o=open(name,"w")
        o.write(input("enter your detail its store in file:"))
        o.close()
    elif choice=='3':
        name=input("Enter Your File Name : \n")
        print("read by file:")
        with open(name,"r") as file:
            for i in file:
                print(i)
    elif choice=="4":
        name=input("Enter Your File Name : \n")
        o=open(name,"a")
        o.write(input("Enter your Append Input here:"))
        o.close()
    elif choice=='5':
        break
    else:
        print("Enter Correct choice : ")
'''
# Writing to a file
with open('example.txt', 'w') as file:
    file.write("Hello, this is a sample file.\n")
    file.write("File handling in Python is simple.\n")

print("File has been written successfully!")

# Reading from the file
with open('example.txt', 'r') as file:
    content = file.read()

print("Reading from the file:")
print(content)'''
