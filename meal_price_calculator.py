

children = float(input("What is the price of a child's meal? "))
adults = float(input("What is the price of an adult's meal? "))
number_of_children = int(input("How many children are there? "))
number_of_adults = int(input("How many adults are there? "))

children_subtotal = children * number_of_children
adults_subtotal = adults * number_of_adults

subtotal = children_subtotal + adults_subtotal

print(f"The subtotal is ${subtotal:.2f}")

tax = float(input("What is the sales tax rate (e.g., 6 or 6.5)? "))

sales_tax = subtotal * tax / 100

total_price = subtotal + sales_tax
print(f"The total price is ${total_price:.2f}")

payment_amount = float(input("What is the payment amount? "))
change = payment_amount - total_price

print(f"The change is ${change:.2f}. \n Thank you for dining with us!")
