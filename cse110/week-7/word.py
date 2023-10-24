import random

words = ['tiger', 'paper', 'battleship', 'puppies', 'lunch'] #string

""" One way to get a random item for the list:
Way 1A: index = random.randint(0, len(words) - 1)
    - random.randint automatically pulls word from index
    - using len(words) - 1 will automatically select one of the words """

""" Way 1B: word = words[index] #this needs to be added for the index of words to be pulled"""

word = random.choice(words) #'word' is a string data type

guesses = ''
lives = 7

while lives > 0:
    print(f'you have {lives} remaining.')
    
    solved = ''

    #putting a letter in-place of an underscore when person guesses a letter correct, or vice versa
    for letter in word:
        if letter in guesses:
            solved += letter
        else:
            solved += '_'

    #if word is completely solved
    if solved == word:
        print('You win')
        break #breaks loop

    #asking the user for their next guess
    guess = input(f'Please guess a letter: {solved}\n').strip().lower()

    #Registers correct guesses in system
    guesses += guess

    if guess in word:
        print(f'Yes, {guess.upper()} is in the word!')
        continue

    #When they guess a number wrong
    print(f'Sorry, {guess.upper()} is not in the word.')
    lives -= 1

#if they lost all of their lives
if lives < 1:
    print('Game over.')