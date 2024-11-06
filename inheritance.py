'''
class dad():
    def phone(self):
        print("Dads phone")

class mom():
    def sweet(self):
        print("Mom's Sweet")
class son(dad,mom): #Multiple inheritance =>one class 
    def laptop(self):
        print("son's laptop")
ram=son()
ram.phone()
ram.sweet()
print("--------------------------------------------------------------------")
class laptop():
    def hp(self):
        print("8GB Ram")
class ram(laptop):  #single inheritance
    def dell(self):
        print("Ram's phone")
s1=ram()
s1.hp() 
print("--------------------------------------------------------------------")
class grandpa():
    def phone(self):
        print("Grandpa phone")
class dad(grandpa):
    def money(self):
        print("Dads Money")
class son(dad,grandpa):
    def laptop(self):
        print("Son's laptop")
ram=son()
ram.laptop()            #Multiple inheritance =>one class 
ram.money()
ram.phone()
daddy=dad()
daddy.phone()
print("-------------------------------------------------------------------------")
class dad():     #hierarichical inheritance => single class occupy whole classes 
    def money(self):
        print("Dad Money")
class son1(dad):
    pass
class son2(dad):
    pass
class son3(dad):
    pass
s1=son1()
s1.money()
print("----------------------------------------------------------------------------")
class dad():      
    def money(self):
        print("Dad Money")
class land():
    def important(self):
        print("Importand land")
class son1(dad,land):
    pass
class son2(dad):            #dad =son1,son2,son3
    pass                    #son1=land,dad => multilevel inheritance
class son3(dad):
    pass
s1=son1()
s1.money()
s1.important()
print("-----------------------------------------------------------------------------")
#single,multiple,multilevel=> Hybrid Inheritance
'''

class animal():
    def __init__(self,name):
        self.name=name 
        def speak():
            pass
class dog(animal):
    def speak(self):
        return f"{name}says woow!"
class cat (animal):
    def speak(self):
        return f"{name} says meow!"
Dog=dog("Buddy")
Cat=cat("whiskers")
print(Dog(self.name))
print(Cat(self.name))









    

