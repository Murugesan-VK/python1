'''A Constructor is a unique function that gets called automatically.
* when an object is created of a class..
uses : class ku evalo memory allocation venum decide panrathu Constructor '''

class laptop:
    def __init__(self):  #python inbuild function.init automatic function call agum
        print("Hp Laptop")   #The main purpose of a constructor is to initialize or assign values to the data members of that class..
        self.price=0        #Current object denote panrathuku use panra keyword ----self
        self.ram=""         
        self.processor=""
    def display(self):          #method
        print("----------------------------------")
        print("Price:",self.price)
        print("Ram:",self.ram)
        print("Processor:",self.processor)

hp=laptop()
hp.price=50000
hp.ram="8gb"
hp.processor="i5"
print(hp.price)
print(hp.ram)
print(hp.processor)
hp.display()
print("--------------------------------------------------------------------")
class student:      #class
    def __init__(self):     
        self.name="Murugesan"
        self.register_number="22MTCS17"
    def display(self):
        print("Name:",self.name)
        print("Register Number:",self.register_number)
s1=student()    #object
s2=student()
s1.name="Murugan"
s1.register_number="777"

s2.name="Karthi"
s2.register_number="888"


s1.display()
s2.display() 

print("--------------------------------------------------------------------")
class fruit:
    def __init__(self,col):     #constructor 
        self.color=col
apple=fruit("RED")
print(apple.color)
print("--------------------------------------------------------------------")
class teacher:
    def __init__(self,name,reg):
        self.name=name
        self.reg_no=reg
    def display(self):
        print("Name :",self.name)
        print("Register_No:", self.reg_no)
t1=teacher("Raju","357")
t2=teacher("veeran","712")
t1.display()
t2.display()
print("--------------------------------------------------------------------")
class calculator:
    def __init__(self,num1,num2):
        self.a=num1
        self.b=num2
    def add(self):
        print("Addition:",self.a+self.b)
    def sub(self):
        print("Subtraction:",self.a-self.b)
    def mul(self):
        print("Multiplication:",self.a*self.b)
    def div(self):
        print("Division:",self.a/self.b)
p1=calculator(12,5)
p1.add()
p1.sub()
p1.mul()
p1.div()
print("--------------------------------------------------------------------")










 
