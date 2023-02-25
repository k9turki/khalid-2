class car():
    name= ""
    model= 0000
    color= ""
    price= 0000

    '''car1= car()
    car1.name= "opel"
    car1.model= 1989
    car1.color="Blue"
    car1.price= 2500
    
    print(car1.name)'''


    '''def __init__(self, name, model, color, price):
        self.name= name
        self.model= model
        self.color= color
        self.price= price
car1= car("opel", 1989, "Blue", 2000)
car2= car("kia", 2005, "Red", 7000)'''

###########

import math
class circle():
    def __init__(self,radius):
        self.radius= radius
    def area(self):
        area= self.radius ** 2 * math.pi
        return area
    def circumference(self):
        circumference= self.radius* 2 * math.pi

        return circumference

c1= circle(5)
c2= circle(10)
print(c1.area())
print(c2.circumference())



