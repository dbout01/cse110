# LAST WEEK'S PROVE ASSIGNMENT HELP #

word = 'cat'

guess = 'bat'


i = 0

solved = ''

0 < 3

#SOLUTION USING A WHILE LOOP
while i < len(word):
    if word[i] == guess[i]:
        solved += f' {guess[i].upper()}'
    elif guess[i] in word:
        solved += f' {guess[i].lower()}'
    else:
        solved += ' _ '
    i += 1



print(solved)


#SOLUTION USING A FOR LOOP; for [index], [var] in enumerate ([list]/[str])
for char in enumerate(word):
    if char == guess[i]:
        solved += f' {guess[i].upper()}'
    elif guess[i] in word:
        solved += f' {guess[i].lower()}'
    else:
        solved += ' _ '

print(solved)