friends = []

name = ""

friends.append("")

while name != 'end':
    name = input("Type the name of a friend: ")

    if name != 'end':
        friends.append(name)

#could also use friends.pop - 'pop' removes last output

for _ in friends: #_ signifies items being printed on new line #use 'friends' instead of 'list'
    print(_)