import zoo_tickets_module

tickets_prices = {
    'baby' : 0.0,
    'kid' : 14.0,
    'adult' : 23.00,
    'senior' : 18.00
    }

total_tickets = {
    'baby' : 0,
    'kid' : 0,
    'adult' : 0,
    'senior' : 0
    }

amount_of_tickets = {
    'baby' : {
        'tickets_number' : (4, 15),
        'tickets_price' : (4, 19)
        },
    'kid' : {
        'tickets_number' : (5, 15),
        'tickets_price' : (5, 19)
        },
    'adult' : {
        'tickets_number' : (6, 15),
        'tickets_price' : (6, 19)
        },
    'senior' : {
        'tickets_number' : (7, 15),
        'tickets_price' : (7, 19)
        }
    }

def ticket_type_identifier(age):
    if age > 0 and age <= 2:
        ticket_type = 'baby'
    elif age <= 12:
        ticket_type = 'kid'
    elif age < 65:
        ticket_type = 'adult'
    else:
        ticket_type = 'senior'
    return ticket_type

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
        zoo_tickets_module.locate_on_display(25, 1)
        print("Wrong age", end = "")
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

def data_print():
    zoo_tickets_module.clear_display()
    print_on_screen()

    age = age_imput()
    total_price = 0

    while age != 0:
        ticket_type = ticket_type_identifier(age)
        ticket_price = tickets_prices[ticket_type]
        total_tickets[ticket_type] += 1 

        zoo_tickets_module.locate_on_display(amount_of_tickets[ticket_type]['tickets_number'][0], amount_of_tickets[ticket_type]['tickets_number'][1])
        print(total_tickets[ticket_type])

        zoo_tickets_module.locate_on_display(amount_of_tickets[ticket_type]['tickets_price'][0], amount_of_tickets[ticket_type]['tickets_price'][1])
        print("{:7.2f}$".format(total_tickets[ticket_type] * ticket_price))

        total_price += ticket_price
        zoo_tickets_module.locate_on_display(9, 19)
        print("{:7.2f}$".format(total_price))

        age = age_imput()

    zoo_tickets_module.locate_on_display(11, 1)
data_print()
