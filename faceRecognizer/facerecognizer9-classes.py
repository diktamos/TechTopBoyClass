class Rectangle:
    def __init__(self,color,w,l):
        self.width = w
        self.length = l
        self.color = color
        
    
    def area(self):
        self.area = self.width*self.length
        return self.area

c1,w1,l1 = 'red',3,4
rect1 = Rectangle(c1,w1,l1)
print('Rectangle 1 is',rect1.color,'width length',rect1.width,rect1.length)
print(rect1.area())