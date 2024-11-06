'''Types of variable in class
    * Instance Variable
    * Class Variable'''
class phone:        #self(t1) = object of instance or self refers object
    ram="8Gb"   #class variable
    def __init__(self,brand,price,chargertype):
        self.brand=brand    #constructor use panna instance variable 
        self.price=price
        self.chargertype=chargertype
    def display(self):
        print(self.brand)
        print(self.price)
        print(self.chargertype)
        print(self.ram)
phone.ram="16GB" #suddenly  ram change into 16gb  
t1=phone("Oppo f19pro",20000,"C-type")
t1.display()
r1=phone("Readme",15000,"B-type")
r1.display()
    
        
