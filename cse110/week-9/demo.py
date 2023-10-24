shopping_list = []

print('Shopping List App')


while True:
    item = input('Add to list: ').strip().lower()

    if item == 'end':
        break

    shopping_list.append(item)

    print('Your Shopping List')

    shopping_list.sort()

    for i, item in enumerate(shopping_list):
        print(f'{i+1}. {item.title()}')