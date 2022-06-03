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
