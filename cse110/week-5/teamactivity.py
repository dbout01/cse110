# A >= 90

# B >= 80

# C >= 70

# D >= 60

# F < 60


grade = float(input('What is your grade percentage?: '))
letter_grade = 'F'

if grade >= 90:
    letter_grade = 'A'
elif grade >= 80:
    letter_grade = 'B'
elif grade >= 70:
    letter_grade = 'C'
elif grade >= 60:
    letter_grade = 'D'


sign = ''
last_digit = grade % 10 #10 is based on a scale from 0s to 100s


if last_digit >= 7:
    sign = '+'
elif last_digit <= 7:
    sign = '-'
else:
    sign = ''


if grade >= 100:
    sign = '+'
else:
        sign = ''
print(f'Your grade is {letter_grade}')