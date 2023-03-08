from math import pi
from math import tan

def AreaPolygon(a,b):
    print("The area of the polygon:",int(a * (b**2) / (4*tan(pi / a)) ))


side = int(input("Input number of sides: "))
length = int(input("Input the length of a side: "))

AreaPolygon(side, length)