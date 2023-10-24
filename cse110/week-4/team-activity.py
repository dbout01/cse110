import math
from tkinter import VERTICAL
print()
print()
print('Welcome to the velocity calculator. Please enter the following:')
print()
mass = float(input('Mass (in kg): '))
gravity = float(input('Gravity (in m/s^2, 9.8 for Earth, 24 for Jupiter): '))
time = float(input('Time (in seconds): '))
fluid_density = float(input('Density of the fluid (in kg/m^3, 1.3 for air, 1000 for water): '))
cross_sec_area = float(input('Cross sectional area (in m^2): '))
drag_const = float(input('Drag constant (0.5 for sphere, 1.1 for cylinder): '))

# Calculates value for inner value c
c = (1 / 2) * fluid_density * cross_sec_area * drag_const
print(f'\nThe inner value of c is: {c:.3f}')


# Compute velocity
velocity = math.sqrt(mass * gravity / c) * (1 - math.exp((-math.sqrt(mass * gravity * c)/mass) * time))
print(f'The velocity after {time} seconds is: {velocity:.3f}m/s')
print()
print()

# Find the cross sectional area of a bowling ball
# (math.pi*r^2)
# skydiver: 1.0 horizontal

# v_terminal = (math.sqrt(mass * gravity) / c )


# stretch challenge with classmates######################