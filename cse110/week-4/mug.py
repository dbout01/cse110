import math

radius = float(input('What is the radius of your mug?: '))
height = float(input('What is the height of your mug?: '))

cubic_inches = (math.pi * (radius ** 2)) * height
    # function for math formula

oz = math.floor(cubic_inches * .554113)

cups = math.floor(oz / 8)

output = f"""
A mug with a radius of {radius}" and a height of {height}" will be:
> {oz} ounces
> {cups} cups
"""
print(output)

# math.floor(#)= rounds down
# "_".cell(#) = rounds up