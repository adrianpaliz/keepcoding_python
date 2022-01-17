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

line_number_baby = 0
line_number_kid = 0
line_number_adult = 0
line_number_senior = 0

while age != 0:
    ticket_price = ticket_price_calculation(age)
    if ticket_price == 0:
        line = 4
        line_number_baby += 1
        zoo_tickets_module.locate_on_display(line, 1)
        print("Ticket price: {} \tTickets number: {}".format(ticket_price, line_number_baby))
    if ticket_price == 14:
        line = 5
        line_number_kid += 1
        zoo_tickets_module.locate_on_display(line, 1)
        print("Ticket price: {}\tTickets number: {}".format(ticket_price, line_number_kid))
    if ticket_price == 23:
        line = 6
        line_number_adult += 1
        zoo_tickets_module.locate_on_display(line, 1)
        print("Ticket price: {}\tTickets number: {}".format(ticket_price, line_number_adult))
    if ticket_price == 18:
        line = 7
        line_number_senior += 1
        zoo_tickets_module.locate_on_display(line, 1)
        print("Ticket price: {}\tTickets number: {}".format(ticket_price, line_number_senior))
    line += 1
    total_price += ticket_price

    age = age_imput()

zoo_tickets_module.locate_on_display(line, 1)
print("Total: {}".format(total_price))
