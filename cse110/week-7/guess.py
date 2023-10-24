import random

# random.randint(start, end) - will generate random number each time & user has to find out what it is
number = random.randint(1, 10)

number = 7

guesses = 5

print('Let\'s play a game')


while True:

    if guesses < 1:
        print('GAME OVER')
        break
    
    guess = int(input('Please guess a number between 1 and 10:\n'))

    if guess < 1 or guess > 10:
        guesses -= 1
        print("Please choose a number between 1 and 10 only!")
        continue
    elif guess == number:
        print('You guessed my number!')
        break
    guesses -= 1
    print(f'Please try again. You have {guesses} guesses left.')

#option 2

    if guess == number:
        print('You guessed my number!')
        break
    print('please try aGAIN')

#option 3

    if guess != number:
        print('Please guess again')
        continue
    print('You guessed my number!')
    break

















