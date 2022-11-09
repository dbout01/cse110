itemz = []

number = ""

print()
print("Welcome to the Shopping Cart Program!")
print()
while number != '5':
    number = input("""Please select one of the following:
    1. Add item
    2. View cart
    3. Remove item
    4. Compute total
    5. Quit
    """)

    for _ in itemz:
        print(_)

    itemz.append("")