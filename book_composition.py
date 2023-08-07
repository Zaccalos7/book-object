from abc import ABC
from pprint import pprint

class Book():
    
    def __init__(self, title, price, authorfname, authorlname):
        
        self.title= title
        self.price= price
        self.authorfname= authorfname
        self.authorlname= authorlname
        
        self.chapters= []
    
    def addchapter(self, name, page):
        self.chapters.append((name, page))
    
    def print_chapters(self):
        print("Chapters")
        for   arg in self.chapters:
            print(arg) 




p1=Book("ciao", 12, "Bill", "Thompson")
p1.addchapter("il millone", 34)
p1.addchapter("il fatone", 31)
p1.addchapter("il dillo", 2)

p2=Book("hallo", 12, "Bill", "Thompson")
p2.addchapter("il polo", 34)

p1.print_chapters()