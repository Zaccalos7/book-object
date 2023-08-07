class Book:
    
    BOOK_TYPE=("comic","divino")
    
    __booklist=None
    
    """booktype: 
    comic","divino" """
    def __init__(self, name, price,booktype):
        self.name=name 
        self.price=price
        if booktype not in Book.BOOK_TYPE:
            raise ValueError(f'{self.booktype} not in book type')
        else:
            self.booktype=booktype
    def __str__(self):
        return f'{self.name}-->{self.price}€'   
    
    def getdiscount(self):
        #check discount
        if hasattr(self,'_discount'):
            self.price= self.price -(self.price * self._discount)
            return self.price
        else:
            return self.price
    
    def setdiscount(self,amount):
        self._discount=amount
        
    @classmethod
    def get_type(cls):
        print("\t", sep=' ')
        return cls.BOOK_TYPE
    
    @staticmethod
    def getbooklist():
        if Book.__booklist==None:
            Book.__booklist=[]
        return Book.__booklist
        


    
b1=Book("Divina Coomedia",100, "divino")
b2=Book("Il codice da vinci",70,"comic")
b1.setdiscount(0.25)
print(b1)
print(b1.getdiscount())
print(b1)
thisbook=Book.getbooklist()
thisbook.append(b1)
thisbook.append(b2)
print(thisbook)