# A >= 90

# B >= 80

# C >= 70

# D >= 60

# F < 60



gradeper = float(input('What is your grade?: '))

if gradeper >= 90:
    print('You have an A')
elif gradeper >= 80:
    print('You have a B')
elif gradeper >= 70:
    print('You have a C')
elif gradeper >= 60:
    print('You have a D')
elif gradeper < 60:
    print('You have a F')