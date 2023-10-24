"""

RANGES
(can be used in different ways / automatically creates a list for us)
Types of ranges
    range(end) - automatically starts at 0
    range(start, end)
    range(start, end, increment)

this is how 'for' loop works:
for [var] in [list]

"""


numbers = range(1, 11)

for num in numbers:
    print(num)



"""LISTS"""
#           0       1       2
colors = ['Red', 'White', 'Blue'] #this is a List, aka Array

for color in colors:
    print(color)

print(colors[1]) #use same brackets used in list and put number in there


#           OR


#for [index], [var] in enumerate([list])
for i, color in enumerate(colors):
    print(f'Index {i} is {color} <=> {colors[i]}') #reaching out to 