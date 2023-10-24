print()
child = float(input("What is the price of a child's meal?: "))
adult = float(input("What is the price of an adult's meal?: "))
childrennum = int(input("How many children are there?: "))
adultnum = int(input("How many adults are there?: "))
salestax = float(input("What is the sales tax rate?: "))
drink = float(input("What is the drink price?: "))
drinknum = int(input("How many drinks are there?: "))
appetizer = float(input("What is the appetizer price?: "))
appetizernum = int(input("how many appetizers are there?: "))
laborsur = float(input("What is the labor surcharge (in cents [.##])?: "))
creditcardsur = float(input("What is the credit card surcharge (in cents [.##])?: "))

print()

child_subtotal= childrennum * child
adult_subtotal = adultnum + adult
drink_subtotal = drinknum * drink
appetizer_subtotal = appetizernum * appetizer
subtotal = child_subtotal + adult_subtotal + drink_subtotal + appetizernum
print(f"Subtotal: ${subtotal:.2f}")

sales_tax = subtotal * salestax / 100
print(f"Sales Tax: ${sales_tax:.2f}")

labor_total = sales_tax + laborsur
print(f"Labor Surcharge: ${labor_total:.2f}")

creditcard_total = labor_total + creditcardsur
print(f"Credit Card Surcharge: ${creditcard_total:.2f}")

total = subtotal + sales_tax + labor_total + creditcard_total
print(f"Total: ${total:.2f}")

print()

paymentamt = float(input("What is the payment amount?: "))
change = paymentamt - total
print(f"Change: ${change:.2f}")