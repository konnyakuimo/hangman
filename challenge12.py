#1
class Apple:
    def __init__(self,w,c,m,s):
        self.weight=w
        self.color=c
        self.money=m
        self.sweet=s
        print("Created!")

ap1=Apple(100,"red",200,True)
print(ap1.sweet)

#2
import math
class Circle:
    def __init__(self,r):
        self.radius=r
        print("Created!")
    def area(self):
        return self.radius*self.radius*math.pi
cir1=Circle(5)
print(cir1.area())
#3
class Triangle:
    def __init__(self,b,h):
        self.bottom=b
        self.height=h
        print("Created!")
    def area2(self):
        return (self.bottom*self.height)/2
tri1=Triangle(5,7)
print(tri1.area2())
#4
class Hexagon:
    def __init__(self,s):
        self.side=s
        print("Created")
    def calculater_perimeter(self):
        return self.side*6
hex1=Hexagon(8)
print(hex1.calculater_perimeter())
