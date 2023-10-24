# INT #

name = input('Hello, what is your name? ')
age = input(f'hello {name}! How old are you? ')
# OR input(input(f'hello {name}! How old are you? '))

age = int(age) * 3
# int(integer) = constructs an integer number from an integer literal, a float literal (by removing all decimals), or a string literal (providing the string represents a whole number)
# int converts age to math and times 3

print(f"{name} is {age * 3} years old")






# ROUND #

number = float(input('...'))
r = round(number, 2)
x = round(number, 2)
print(x)



# ARITHMETIC OPERATORS #

# + 	Addition 	           ex: x + y 	
# - 	Subtraction 	       ex: x - y 	
# * 	Multiplication 	       ex: x * y 	
# / 	Division 	           ex: x / y 	
# % 	Modulus 	           ex: x % y 	
# ** 	Exponentiation 	       ex: x ** y 	
# // 	Floor division 	       ex: x // y