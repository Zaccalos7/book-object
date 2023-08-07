class Pubblication():
    def __init__(self, title, price):
        self.title=title
        self.price=price
        
        
class Book(Pubblication):
    def __init__(self, author, pages, title, price):
        super().__init__(title,price)
        self.author=author 
        self.pages=pages