#import random words to string
import random

random_words = ("christmas", "snow", "cookies", "wine", "Jesus", "carol") #string
secret_word = random.choice(random_words) #selects a random word
guess = "" #quotes only indicate that user inputs a word
guess_count = 0 #tracks how many guesses a user has made
hint = "_ " * len(secret_word) #underscores show how many letters there are

wrong_list = [] #helps etablish an output for when a user guesses a wrong letter

print("Welcome to the guessing game! Think Chrirstmas.")
print()

while guess != secret_word: #sets up the function that determines if you guess was valid or not
    print(f'Your hint is {hint}')
    guess = input('What is your guess?: ').lower()
    guess_count = guess_count + 1

    if len(guess) != len(secret_word): #looks to see if what you guessed isn't equal to number of letters in secret word
        print("The word is not the right length!")
    
    elif(guess in wrong_list): #helps the user choose a different letter if they made this by mistake
        print('You already guessed this letter.')

if secret_word == guess: #establishes the correct word found
    print('Congratulations! You guessed it!')
    print(f'It took you {guess_count} guesses to get it right!')