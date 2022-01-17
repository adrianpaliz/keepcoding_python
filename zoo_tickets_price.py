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

zoo_tickets_module.clear_display()

age = age_imput()

total_price = 0

line = 4

while age != 0:
    ticket_price = ticket_price_calculation(age)
    zoo_tickets_module.locate_on_display(line, 1)
    print("Ticket price: {}".format(ticket_price))
    line += 1
    total_price += ticket_price

    age = age_imput()

zoo_tickets_module.locate_on_display(line, 8)
print("Total: {}".format(total_price))
