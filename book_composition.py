from abc import ABC
from pprint import pprint

class Book():
    
    def __init__(self, title, price, author=None):
        
        self.title= title
        self.price= price
        self.author= author
        
        self.chapters= []
    
    def addchapter(self, chapter):
        self.chapters.append((chapter))
    
    def print_chapters(self):
        print("Chapters")
        for   args in self.chapters:
            print(args) 


class Author():
    
    def __init__(self, fname, lname):
        self.fname= fname
        self.lname= lname
    
    def __str__(self):
        return f'{self.fname} {self.lname}'
    
class Chapter():
    def __init__(self, name, pagecount):
        self.name= name
        self.pagecount= pagecount
        
    def __str__(self):
        return f'{self.name} {self.pagecount}'
# p1=Book("ciao", 12, "Bill", "Thompson")
# p1.addchapter("il millone", 34)
# p1.addchapter("il fatone", 31)
# p1.addchapter("il dillo", 2)

# p2=Book("hallo", 12, "Bill", "Thompson")
# p2.addchapter("il polo", 34)

# p1.print_chapters()

filippo=Author("Filippo", "Pirozzi")
print(filippo)

p1=Book("ciao", 12, filippo)
c1=Chapter("il risveglio", 120)
c2=Chapter("il suono delle sirene", 123)
c3=Chapter("oronzo", 20)

p1.addchapter(c1)
p1.addchapter(c2)
p1.addchapter(c3)
p1.print_chapters()
print(p1.author)