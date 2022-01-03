units_input = input("Amount: ")
units_float = float(units_input)

price_input = input("Unit price: ")
price_float = float(price_input)

total_items = 0
total_price = 0

print_lines = "\n"

while units_float > 0 and price_float > 0:
    unitary_total = units_float * price_float
    
    print_lines += str(price_float) + "€ - " + str(units_float) + " units - " + str(unitary_total) + "€\n"
    # Another way for print_lines with .formart
    # print_lines += "{}€ - {} units - {}€\n".format(precio_float, units_float, unitary_total)
    total_items += units_float
    total_price += unitary_total
    
    units_input = input("Amount: ")
    units_float = float(units_input)
    price_input = input("Unit price (€): ")
    price_float = float(price_input)

print(print_lines)
print("-------------------")
print("Total:", total_price)
print("Units:", total_items)