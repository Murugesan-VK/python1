#Class: is a set of functions and variables
#Object: Instance of class..
class collegeadmission:     # Class = collegeadmission 
    name=""                 # Objects = ramesh,suresh
    age=""                  # Variables = name,age,course =>while using default values
    course="Bsc chemistry"  
    def trichy(self):
        print("Bharathidasan University")
    def pudukkottai(self):
        print("JJ college")
ramesh=collegeadmission() 
suresh=collegeadmission() 

ramesh.trichy()
suresh.pudukkottai()
print("-----------------------------")
ramesh.name="Rohit"
ramesh.age=19
print("Name:",ramesh.name)
print("Age:",ramesh.age)
print("Course:",ramesh.course)
ramesh.trichy()
print("-----------------------------")
suresh.name="Dhoni"
suresh.age=20
print("Name:",suresh.name)
print("Age:",suresh.age)
print("Course:",suresh.course)
suresh.pudukkottai()
print("-----------------------------------------------------------------------")
class laptop:
    price=""         
    processor=""
    Ram=""
    def trichy(self):
        print("2 Years Guaranty")
hp=laptop()
dell=laptop()
lenovo=laptop()
print("--------------------------")
hp.price="62,000"
hp.processor="I5"
hp.ram="8gb"
print(hp.price)
print(hp.processor)
print(hp.ram)
hp.trichy()
print("--------------------------")
dell.price="25,000"
dell.processor="I4"
dell.ram="4gb"
print(dell.price)
print(dell.processor)
print(dell.ram)
dell.trichy()
print("--------------------------")
lenovo.price="10,000"
lenovo.processor="I3"
lenovo.ram="2gb"
print(lenovo.price)
print(lenovo.processor)
print(lenovo.ram)
lenovo.trichy()
print("-----------------------------------------------------------------------")
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

