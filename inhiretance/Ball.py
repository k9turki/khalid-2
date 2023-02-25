import math
from inhiretance.Circle import Circle
class Ball(Circle):
    def __init__(self, radius):
        self.radius= radius

    def volume(self):
        BA= (4*math.pi)/3 * self.radius** 3
        return BA
    def area(self):
        area= self.radius ** 2 * math.pi
        return area
    def print_area_1(self):
        print("The area for (son) is", str(self.area()))
        return
    def print_area_2(self):
        print("The area for (father) is", str(super().area()))

        return


