import math
class Circle():
    def __init__(self,radius):
        self.radius= radius

    def circumference(self):
        circumference= self.radius* 2 * math.pi

        return circumference
    def area(self):
        area= self.radius ** 2 * math.pi
        return area

