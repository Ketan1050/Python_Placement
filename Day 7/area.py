"""" 
Method Overroding 
"""
class Triangle():
    def __init__(self,base,height):
        self.base = base
        self.height = height
        
    def getArea(self):
        print(self.base*self.height/2,"is area of triangle")
        
class Square(Triangle):
    def __init__(self,side):
        self.side = side
        Triangle.__init__(self,side,side)
        
    # def getArea(self):
    #     print(self.side*self.side,"is area of square")
        
        
t = Triangle(2,6)
s = Square(4)
t.getArea()
s.getArea() 

#make three object of the class square 
s1 = Square(5)
s2 = Square(6)
s3 = Square(7) 
s1.getArea()
s2.getArea()     

#check if the objects are equal or not 
print(s1 == s2)
print(s1 == s3) #check if the objects are equal or not 
print(s2 is s3) #check if the objects are of same type or not 
print(s2.getArea()) 