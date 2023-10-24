# from unicodedata import numeric


# scope = 'A'

# num = int(input('Please choose a number: '))

# if num  < 10:
#     scope = 'A1'
#     if num < 0:
#         print(f'{num} is less than 10 and is negative.')
#     else:
#         scope = 'A2'
#     print(f'{num} is less than 10.')
# elif num == 10:
#     scope = 'B'
#     print(f'{num} is equal than 10. ')
# else:
#     scope = 'C'
#     print(f'{num} is greater than 10.')

# print(scope)



ans = input('Is the sky blue? ')

if 'yes' in ans.lower():
    print('Correct!')
else:
    print('You\'re incorrect. You might be colour blind.')


while True:
    try:
        age = input('Are you 18 years or older? ')
    except ValueError:
        print("Sorry, I didn't understand that. Please type [yes] or [no].\n")
        continue
    if 'yes' in ans.lower():
        print('Welcome! you may enter.')
        break
    if 'no' in ans.lower():
        print('YOU SHALL NOT ENTER.')
        break



# ans = input('Are you 18 years or older? ')

# if 'yes' in ans and len(ans.strip()) <= 3:
#     print('You may enter')
# else:
#     print('Go away')


# a = -3

# if False:
#     -> # ...
# ->