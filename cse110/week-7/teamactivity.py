import random

number = random.randint(-100, 100)

guess = ''
number = 18
guesses = 6

while number != guess:
    guess = int(input('What is the magic number?: '))

    if guesses == 0:
        print('GAME OVER')
        break
    
    if guess < 18:
        guesses -= 1
        print("Higher!")
        continue
    guesses -= 1

    if guess > 18:
        guesses -= 1
        print('Lower!')
        continue
    guesses -= 1
print(f'You guessed it! Would you like to play again?')