import math

#Square

square_side_length = float(input("What is the length of the side of the square (in cm)?: "))
square_area = square_side_length ** 2
print(f"The area of the square is: {square_area / 1000} m^2")

print()

#Rectangle
rectangle_length = float(input("What is the length of rectangle (in cm)?: "))
rectangle_width = float(input("What is the width of rectangle (in cm)?: "))
rectangle_area = rectangle_length * rectangle_width

print(f"The area of the rectangle is: {rectangle_area / 1000} m^2")

print()

#Circle
circle_radius = float(input("What is the radius of the circle (in cm)?: "))
circle_area = math.pi * circle_radius ** 2

print(f"The area of the circle is: {circle_area / 1000: .2f} m^2" )