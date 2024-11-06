class laptop:
    ram="8GB" #self use panni enghalam function create panrom oh atha instance method
    def __init__(self):
        self.brand=""
        self.price=10000
    def setprice(self,price):
        self.price=price
    def getprice(self):     #instance method
        print("Price:",self.price)
    @classmethod #decorators #class method
    def setram(cls): #class variable access panrathukku cls use pannannum
        cls.ram="16GB"
        print("Change-Ram 8GB into 16GB")
    @staticmethod   #static method
    def info():
        print("This is laptop class")
hp=laptop()
hp.setprice(20000)
hp.getprice()
laptop.setram()
hp.info()
