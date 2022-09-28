import math

#Square

square_side_length = float(input("What is the length of the side of the square?: "))

square_area = square_side_length ** 2
print(square_area)

print()
#Rectangle
rectangle_length = float(input("What is the length of rectangle?: "))
rectangle_width = float(input("What is the width of rectangle?: "))

rectangle_area = rectangle_length * rectangle_width

print(rectangle_area)

print()
#Circle
circle_radius = float(input("What is the radius of the circle?: "))
circle_area = math.pi * circle_radius ** 2

print(f"The area of the circle is {circle_area:.2f}" )