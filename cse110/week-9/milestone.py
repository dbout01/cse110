shopping_list = []

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

        if selection == "1":
            item = input("What item would you like to add?: ")
            shopping_list.append(item)
            print(item + " has been added to the cart.")    

        elif selection == "2":
            print()
            print("The contents of the shopping cart are: ")
            for i in shopping_list:
                print(i)

        elif selection == "5":
            print('Thank you. Goodbye.')
            break
        
        else:
            print("Invalid selection.")