# ...

# get details for the order
amount = int(input('How many business cards do you need?: '))
chr_count_front = int(input('How many characters are on the front?: '))
chr_count_back = int(input('How many characters are on the back?: '))

# calculate the order cost.
card_stock = .15
card_ink = .003 #.003 is dynamic
markup = .30

cost = card_stock * markup # base cost
cost += card_ink * markup * \
    (chr_count_front + chr_count_back) #() adds both together and then * the rest
cost *= amount # order cost * order amount
cost += cost * markup #markup order cost


print(f"Order total: ${cost:.3g}")