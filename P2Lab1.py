#Davis,Cornelius
#25Feb2025
#P2Lab1
#Finding the radius

import math

radius = float(input("what is the radius of the circle: "))

diameter = 2*radius

circumference = 2*math.pi*radius

area = math.pi*radius**2

print(f"the diameter of the circle is: {diameter:.1f}")

print()

print(f"the circumference of the circle is: {circumference:.2f}")

print()

print(f"the area of the circle is: {area:.3f}")
