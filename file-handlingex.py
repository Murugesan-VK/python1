while True:
    choice=input("1.createFile\n2.WriteFile\n3.readFile\n4.AppendFile\n5.Exit")
    if choice=="1":
        name=input("Enter Your File Name\n")
        o=open(name,"w")
        # o.write("yes its worked\n")
        # o.close()
        break
    elif choice=='2':
        name=input("Enter Your File Name\n")
        o=open(name,"w")
        o.write(input("enter your detail its store in file:"))
        o.close()
    elif choice=='3':
        name=input("Enter Your File Name\n")
        print("read by file:")
        with open(name,"r") as file:
            for i in file:
                print(i)
    elif choice=="4":
        name=input("Enter Your File Name\n")
        o=open(name,"a")
        o.write(input("Enter your Append Input here:"))
        o.close()
    elif choice=='5':
        break
    else:
        print("Enter Correct choice")
