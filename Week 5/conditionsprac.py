from unicodedata import numeric


scope = 'A'

num = int(input('Please choose a number: '))

if num  < 10:
    scope = 'A1'
    if num < 0:
        print(f'{num} is less than 10 and is negative.')
    else:
        scope = 'A2'
    print(f'{num} is less than 10.')
elif num == 10:
    scope = 'B'
    print(f'{num} is equal than 10. ')
else:
    scope = 'C'
    print(f'{num} is greater than 10.')

print(scope)