class company():
    def __init__(self):
        self.__companyname="Google" #private variable access within in a class or do not access without class
    def companyname(self):          #public
        print(self.__companyname)  #(__) private 

c1=company()
c1.companyname() #Enacapsulation
#print(c1._companyname)
print("---------------------------------------------------------------------")
class company():
    def __init__(self):
        self._companyname="Google"  #protected variable can access in child class
    def companyname(self):          
        print(self._companyname)  #(_) protected 
class b(company):
    pass
b1=b()
c1=company()
c1.companyname() #Enacapsulation
#print(c1._companyname)
print("---------------------------------------------------------------------")
