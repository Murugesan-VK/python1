def add(a,b):
    print(a+b)
add(10,20)
print("--------------------------------------------------------------")
def add(a=10):
    print(a)
add(50)
print("--------------------------------------------------------------")
def add(a,b,c=0):       #polymorphism #poly means naraiyaa
    print(a+b+c)        #morphism => function antha antha activity mathikirathu
add(1,2)
add(1,2,3)
print("--------------------------------------------------------------")
'''The Word Polymorphism means having many forms. In programming,polymorphism means
the same function name(but different signatures)being used for different types.
The key difference is the data types and number of arguments used in function.'''
print("--------------------------------------------------------------")
class animal:       #base class or parent class
    def sound(self):
        print("Animals makes sound")
class dog(animal):    #derived class inherit from animal
    def sound(self):
        print("Dog Barks")
class bird(animal):
    def sound(self):
        print("Birds Sing")
a1=animal()
d1=dog()
d1.sound()
a1.sound()
b1=bird()
b1.sound()
print("--------------------------------------------------------------")
class shape:
    def area(self):
        return 0
class rectangle(shape):
    def area(self):
        l=10
        b=20
        return "Area of rectangle:",l*b
s1=shape()
r1=rectangle()
s1.area()
r1.area()
print(r1.area())
print("--------------------------------------------------------------")
class person:
    def __init__(self,name):
        self.name=name
class student(person):
    def __init__(self,name,grade):
        super().__init__(name)
        self.grade=grade
    def display(self):
        print(self.name,self.grade)
s1=student("MURUGAN","A-Grade")
s1.display()
print("--------------------------------------------------------------------------")
class vehicle:
    def start(self):
        print("Vehicle Started")
class car(vehicle):
    def start(self):
        print("Car Started")
c1=car()
c1.start()
print("--------------------------------------------------------------------------")
class employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
class manager(employee):
    def __init__(self,name,salary,department):
        super().__init__(name,salary)
        self.department=department
    def display(self):
        print(self.name,self.salary,self.department)
m1=manager("MURUGAN","20000","CSE")
m1.display()
print("--------------------------------------------------------------------------")

        













































