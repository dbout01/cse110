numbers = [42, 25, 18, 83, 23, 85, 38, 2]

#min(numbers) max(numbers)

min_num = 9999999999
max_num = 0

for number in numbers:
    if number < min_num:
        min_num = number
    if number > max_num:
        max_num  = number

print(f'MIN: {min_num}, MAX: {max_num}')