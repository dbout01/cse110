with open('C:\\Users\dbutt\OneDrive\Desktop\cse110\week-11\books.txt') as f:

    for line in f:
        parts = line.strip().split(' ')
        name = parts[0]
        title = parts[2]
        print(f'Name: {name}, Title: {title}')