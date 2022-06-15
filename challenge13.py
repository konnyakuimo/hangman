#1
class Rectangle:
    def __init__(self,w,l):
        self.wide=w
        self.lenght=l
    def perimeter(self):
        return (self.wide*2)+(self.lenght*2)
class Square:
    def __init__(self,e):
        self.edge=e
    def perimeter(self):
        return self.edge*4
    #2
    def change_size(self,c):
        self.change=c
        self.edge=self.edge-self.change
rec1=Rectangle(12,3)
print(rec1.perimeter())
squ1=Square(15)
print(squ1.perimeter())

#2
squ1.change_size(3)
print(squ1.perimeter())

#3