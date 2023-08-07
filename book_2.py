class Book():
    
    BOOK_TYPE={"Romance","Commedy","Thriller"}
    
    def __init__(self,name,price,booktype):
        self.name=name
        self.price=price
        self.__secret="dont see it "
        
        if booktype not in Book.BOOK_TYPE:
            raise  ValueError(f"{booktype} not in Booktype")
        else:
            self.booktype=booktype
       
        
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
    
    @classmethod
    def gettype(cls):
        print("/t",sep='')
        return cls.BOOK_TYPE
        
    def __str__(self):
        return f'{self.name} (${self.price})'


print(Book.gettype() )       

b1=Book("Python",100,"Romance")
print(b1)

b2=Book("C++",70,"Thriller")
print(b2)
#print(b1.
# getprice())
# b1.setdiscount(0.25)
# print(b1.getprice())
# print(b1._Book__secret)
