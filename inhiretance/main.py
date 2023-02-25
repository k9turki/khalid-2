from inhiretance.Ball import Ball
from inhiretance.Circle import Circle
from inhiretance.Cylinder import Cylinder

b1= Ball(5)
print("b1 volume is", b1.volume())
####################

C2= Circle(3)
print("C2 area is", C2.area())
####################

CY= Cylinder(2,5)
print("CY volume is", CY.volume())
####################

print(b1.print_area_1())
print(b1.print_area_2())
####################

print("the area is :" + str(CY.area()))
print("the mo7ee6 is :" + str(CY.circumference()))
print("the area of the base :" + str(CY.get_base().area()))







