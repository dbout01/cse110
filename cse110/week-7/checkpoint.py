import random

number = random.randint(-20, 20)


guess = ''
number = 12
guesses = 3
candy_yes_no = ''


print('Let\'s play a game')

while number != guess:
    guess = int(input('Guess the number. You have four guesses: '))

    if guesses == 0:
        print('GAME OVER')
        break
    
    if guess < 0:
        guesses -= 1
        print("Sorry that is a negative number! please try again!")
        continue
    guesses -= 1
print(f'the number is {number}')




while candy_yes_no != 'yes':
    candy_yes_no = input('Can I have candy?')
print('Gimme dat candy')