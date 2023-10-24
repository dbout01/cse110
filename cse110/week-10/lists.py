words = ['pizza', 'pie', 'apple', 'bacon', 'cheese']
qty = [5, 9, 7, 1, 1]

qty.sort()

for i, word in enumerate(words):
    print(f'{i+1} {word} x {qty[i]}')

#when making two lists, make sure everything is factored in to change
words.pop(2)
qty.pop(2)

for i, word in enumerate(words):
    print(f'{i+1} {word} x {qty[i]}')




'''
add to list
    words.append('cake')

remove the first element
    first = words.pop('pizza') you can remove by word, index #, position, etc.

remove the last element
    last = words.pop('')
'''