'''
WEEK 7 MILESTONE
'''

secret = "keep"
guess = ""
counter = 0

while guess != secret:
    guess = input('Can you guess what the word is?').strip().lowercase()
    counter += 1
    if guess == secret:
        print('YOU WIN')

    else:
        print('That was not correct. Try again')

print(f'It took you {counter} guesses to get it right!')




'''
WEEK 8 PROVE
'''

secret = "keep"
guess = ""
counter = 0

for i in secret:
    solved += ' _ '

while guess != secret:

    print('You guess is: {solved}')

    guess = input('Can you guess what the word is?').strip().lowercase()

    counter += 1

    if len(guess) != len(secret):
        print('Your guesss was not the correct length!')
        continue

    solved = ''
    
    if guess == secret:
        print('YOU WIN')

    for i, char in enumerate(secret):
        if guess[i] == char:
            solved += f' {char.uppercase()}'
        elif guess[i] in secret:
            solved += f' {char.lowercase()}'
        else:
            solved += ' _ '

print(f'It took you {counter} guesses to get it right!')