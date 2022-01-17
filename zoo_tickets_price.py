import zoo_tickets_module

def ticket_price_calculation(age):
    if age > 0 and age <= 2:
        price = 0
    elif age <= 12:
        price = 14
    elif age < 65:
        price = 23
    else:
        price = 18
    return price

def age_imput_validation(raw_input):
    try:
        integer = int(raw_input)
        if integer >= 0:
            return True
        return False
    except:
        return False

def age_imput():
    zoo_tickets_module.locate_on_display(1, 1)
    age = input("How old you are?: ")
    while age_imput_validation(age) == False:
        print("Wrong age")
        zoo_tickets_module.locate_on_display(1, 1)
        age = input("How old you are?: ")
    return int(age)

def print_on_screen():
    zoo_tickets_module.locate_on_display(4, 5)
    print("Baby....:   -")
    zoo_tickets_module.locate_on_display(5, 5)
    print("Kid.....:   -")
    zoo_tickets_module.locate_on_display(6, 5)
    print("Adult...:   -")
    zoo_tickets_module.locate_on_display(7, 5)
    print("Senior..:   -")

    zoo_tickets_module.locate_on_display(9, 8)
    print("Total....:")

zoo_tickets_module.clear_display()

print_on_screen()

age = age_imput()

total_price = 0

line = 4

while age != 0:
    ticket_price = ticket_price_calculation(age)
    if ticket_price == 0:
        zoo_tickets_module.locate_on_display(4, 15)
        print(1)
        zoo_tickets_module.locate_on_display(4, 19)
        print(ticket_price)

    if ticket_price == 14:
        zoo_tickets_module.locate_on_display(5, 15)
        print(1)
        zoo_tickets_module.locate_on_display(5, 19)
        print(ticket_price)

    if ticket_price == 23:
        zoo_tickets_module.locate_on_display(6, 15)
        print(1)
        zoo_tickets_module.locate_on_display(6, 19)
        print(ticket_price)

    if ticket_price == 18:
        zoo_tickets_module.locate_on_display(7, 15)
        print(1)
        zoo_tickets_module.locate_on_display(7, 19)
        print(ticket_price)

    total_price += ticket_price

    age = age_imput()

zoo_tickets_module.locate_on_display(line, 1)
print("Total: {}".format(total_price))
