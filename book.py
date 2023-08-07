class Book():
    def __init__(self,name,price):
        self.name=name
        self.price=price
        self.__secret="dont see it "
       
        
    def getprice(self):
        if hasattr(self,"_discount"):
            self.price=self.price - (self.price * self._discount)
            print("\tPRICE with discount")
            return self.price
        else:
            print("\t PRICE")
            return self.price
    
    def setdiscount(self,amount):
        self._discount=amount
    
    def __str__(self):
        return f'{self.name} (${self.price})'
        
b1=Book("Python",100)
print(b1)
#print(b1.getprice())
# b1.setdiscount(0.25)
# print(b1.getprice())
# print(b1._Book__secret)
