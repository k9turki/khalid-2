import math

from inhiretance.Circle import Circle


class Cylinder(Circle):
    def __init__(self, radius, height):
        super().__init__(radius)
        self.height= height

    def volume(self):
        CY= math.pi * self.radius ** 2 * self.height
        return CY

    def area(self):
        area= self.circumference() * self.height
        return area

    def get_base(self):
        return super()

    def area_of_base(self):
        return super().area()
