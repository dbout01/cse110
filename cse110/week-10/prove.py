print()
print('Welcome to the Shopping Cart Program!')
menu = ['Add item', 'View Cart', 'Remove an Item', 'View Total', 'Quit']
qty = [1, 1, 1, 1, 1]

cart = []

prices = []


while True:
    for i, option in enumerate(menu):
        print(f'{i +1} {option}')
    
    choice=  0

    try:
        choice = int(input('Please enter an action: '))
    except:
        print('please enter only a number')
        continue

#ADD ITEM
    if choice == 1:
        new_item = input('What would you like to add?: ') #you can add nested while
        cart.append(new_item) #you can add nest menu
        price = float(input(f'What is the price of {new_item}?: '))
        prices.append(price)
        print()
        print(f'{new_item}, ${price}, added!')
        print()
        pass

#VIEW CART
    elif choice == 2:
        print()
        print("The contents of the shopping cart are: ")
        for i in cart:
            print(i)
        pass

#REMOVE AN ITEM
    elif choice == 3:
        old_item = int(input('What is the name of the item to remove?: '))
        try:
            choice = int(input('Type the number you would like: '))
            
        except:
            print('please enter only a number')
        continue

#VIEW TOTAL
    elif choice == 4:
        total = 0
        for item_price in prices:
            total = item_price + total
            print(f'The total price of the items in the shopping cart is ${total:.2f}')
        pass

#QUIT
    elif choice == 5:
         print('Thank you. Goodbye.')
         break

    else:
        print('Please choose a number between 1 and {len(menu)}')