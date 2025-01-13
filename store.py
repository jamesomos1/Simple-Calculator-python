
item = input("What item will you like to buy?:  ")
price = float(input("What is the price?: "))
quantity = int(input("How many would you like?: "))

total = price * quantity

print(f"Yu have bought {quantity} x {item}(s)")
print(f"Your total is: ${round(total, 2)}")