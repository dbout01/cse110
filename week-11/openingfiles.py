#opens file - for me, the whole path needs to be stated in order to be used
with open('C:\\Users\dbutt\OneDrive\Desktop\cse110\week-11\hr.txt') as f:

    for line in f:
        parts = line.strip().split(' ')
        name = parts[0]
        title = parts[2]
        print(f'Name: {name}, Title: {title}')