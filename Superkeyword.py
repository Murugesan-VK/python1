class a():
    def __init__(self):
        print("A")
    def display(self):
        print("You are in class a")
class b():
    def __init__(self):
        print("B")
    def display(self):
        print("You are in class b")
obj=b()
print("-------------------------------------------------------------------")
class a():
    def __init__(self):
        print("A")
    def display(self):
        print("You are in class a")
class b(a): #pass a into self 
    def __init__(self): 
        print("B") # remove constructor then run 
    def display(self):
        print("You are in class b")
obj=b()
print("-------------------------------------------------------------------")
class a():
    def __init__(self):
        print("A")
    def display(self):
        print("You are in class a")
class b(a): #pass a into self 
    def __init__(self):
        super().__init__()  #superkeyword
        print("B")  
    def display(self):
        print("You are in class b")
obj=b()
print("--------------------------------------------------------------------")
class a():
    def __init__(self):
        print("A")
    def display(self):
        print("You are in class a")
class b(): 
    def __init__(self):
        super().__init__()  #superkeyword
        print("B")  
    def display(self):
        print("You are in class b")
class c(b,a): #replace #multiple inheritance eruntha first erukkura variable check pannum()
    def __init__(self):
        super().__init__()
        print("C")  
    def display(self):
        print("You are in class b")

obj=c()

















