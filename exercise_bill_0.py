units_input = input("Amount: ")
units_float = float(units_input)

price_input = input("Unit price: ")
price_float = float(price_input)

total_items = 0
total_price = 0

prices_list = []
units_list = []
while units_float > 0 and price_float > 0:
    unitary_total = units_float * price_float
    prices_list.append(price_float)
    units_list.append(units_float)
    
    total_items += units_float
    total_price += unitary_total
    
    units_input = input("Amount: ")
    units_float = float(units_input)
    price_input = input("Unit price (€): ")
    price_float = float(price_input)

index = 0
while index < len(prices_list):
    print(prices_list[index], "€ - ", units_list[index], "units -", prices_list[index] * units_list[index], "€")
    index += 1

print("-------------------")
print("Total:", total_price)
print("Units:", total_items)