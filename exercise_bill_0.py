units_input = input("Amount: ")
units_float = float(units_input)

price_input = input("Unit price: ")
price_float = float(price_input)

total_items = 0
total_price = 0

while units_float > 0 and price_float > 0:
    unitary_total = units_float * price_float
    print(price_float, "€ -", units_float, "units -", unitary_total, "€")
        
    total_items += units_float
    total_price += unitary_total
    
    units_input = input("Amount: ")
    units_float = float(units_input)
    price_input = input("Unit price (€): ")
    price_float = float(price_input)

print("-------------------")
print("Total:", total_price)
print("Units:", total_items)
