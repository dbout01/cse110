first = int(input("What is the first number?: "))
second = int(input("What is the second number?: "))

if first > second:
    print ('The first number is greater')
elif first < second:
        print('The first number is not greater')

if first == second:
    print('The numbers are equal')
elif first != second:
        print('The numbers are not equal')

if second < first:
    print('The second number is greater')
elif second > first:
        print('The second number is not greater')


print()


user_animal = input("What is your favorite animal? ")

if user_animal.lower() == "dog":
    print('That\'s my favorite animal too!')
else:
    print('You\'re wrong, my friend')