import random

random_words = ("christmas", "snow", "cookies", "wine", "jesus", "carol") #string
secret_word = random.choice(random_words) #selects a random word
print(secret_word)
guess = "" #quotes only indicate that user inputs a word
guess_count = 0 #tracks how many guesses a user has made
hint = "_ " * len(secret_word) #underscores show how many letters there are

wrong_list = [] #helps etablish an output for when a user guesses a wrong letter

print("Welcome to the guessing game! Think Christmas.")
print()

while guess != secret_word: #sets up the function that determines if you guess was valid or not
    print(f'\nYour hint is {hint}')
    guess = input('What is your guess?: ').lower()
    guess_count = guess_count + 1

    if len(guess) != len(secret_word): #looks to see if what you guessed isn't equal to number of letters in secret word
        print("Sorry, the guess must have the same number of letters as the secret word!")

    elif(guess in wrong_list): #helps the user choose a different letter if they made this by mistake
        print('You already guessed this letter.')

    for i in range(len(secret_word)):  #added 'for' to add letter within hint output

        if secret_word[i] == guess[i]: #helps establish that when someone guesses a correct letter within a specific spot, it will print an 'upper'
            print(guess[i].upper() , end="")

        elif guess[i] in secret_word: #helps establish that when someone guesses a correct letter within the word, it will print a 'upper'
            print(guess[i].lower() , end="")

        else:
            print('_' , end="")
    

if secret_word == guess: #establishes that the correct word was found
    print('Congratulations! You guessed it!')
    print(f'It took you {guess_count} guesses to get it right!')