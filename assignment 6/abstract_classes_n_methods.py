from abc import ABC, abstractmethod

# Abstract base class
class Shape(ABC):
    
    @abstractmethod
    def area(self):
        pass  

class Triangle(Shape):
    
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height  

rect = Triangle(5, 10)
print("Area of Triangle:", rect.area())
