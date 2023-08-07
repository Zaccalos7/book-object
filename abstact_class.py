from abc import ABC, abstractmethod

class Perimeter(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def Calc_Perimeter(self):
        pass
    

class Square(Perimeter):
    def __init__(self, side):
        self.side=side
    
    def Calc_Perimeter(self):
        return self.side * self.side
  

class Cirlce(Perimeter):
    def __init__(self, radius):
        self.radius=radius
        
    def Calc_Perimeter(self):
        return 3.14*(self.radius*2)


class Triangle(Perimeter):
    def __init__(self, side_1, side_2, side_3):
        self.side_1=side_1
        self.side_2=side_2
        self.side_3=side_3
    
    def Calc_Perimeter(self):
        return self.side_1 + self.side_3 + self.side_2

triangolo=Triangle(3,4,5)
cerchio=Cirlce(3)
quadrato=Square(4)

print(triangolo.Calc_Perimeter())   
print(cerchio.Calc_Perimeter())   
print(quadrato.Calc_Perimeter())   
    