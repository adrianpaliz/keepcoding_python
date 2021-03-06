units_input = input("Amount: ")
units_float = float(units_input)

price_input = input("Unit price: ")
price_float = float(price_input)

total_items = 0
total_price = 0

bill_lines_list = []

while units_float > 0 and price_float > 0:
    unitary_total = units_float * price_float
    item = dict()
    item['units'] = units_float
    item['price'] = price_float
    
    bill_lines_list.append(item)
        
    total_items += units_float
    total_price += unitary_total
    
    units_input = input("Amount: ")
    units_float = float(units_input)
    price_input = input("Unit price (€): ")
    price_float = float(price_input)

for item in bill_lines_list:
    print(item['price'],"€ -", item['units'], "unidades -", item['units'] * item['price'], "€")

print("-------------------")
print("Total:", total_price)
print("Units:", total_items)