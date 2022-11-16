shopping_list = []

prices = []

number = ''

while number != '5':
        print()
        print("""Welcome to the Shopping Cart Program!

        Please select one of the following:
        1. Add item
        2. View cart
        3. Remove item
        4. Compute total
        5. Quit
        """)

        selection = input("Please enter an action: ")
    #ADD
        if selection == "1":
            item = input("What item would you like to add?: ")
            shopping_list.append(item)
            print(item + " has been added to the cart.")
            price = float(input(f'What is the price of {item}?: '))
            prices.append(price)

    #REMOVE
        elif selection == "3":
            kill = int(input('Which item would you like to remove?: '))

            try:
                choice = int(input('Type the number you would like: '))
            except:
                print('please enter only a number')
            continue



    #TOTAL  
        elif selection == '4':
            total = 0
            for item_price in prices:
                total = item_price + total
                print(f'The total price of the items in the shopping cart is {total:.2f}')