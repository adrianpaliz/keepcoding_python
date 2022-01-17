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
    age = zoo_tickets_module.input_location("How old you are?: ", 1, 1)
    while age_imput_validation(age) == False:
        zoo_tickets_module.text_format(0, 33, 41)
        zoo_tickets_module.print_location("Wrong age", 25, 1, True)
        zoo_tickets_module.reset_text_format()
        age = zoo_tickets_module.input_location("How old you are?: ", 1, 1)

    zoo_tickets_module.clear_line(25)

    return int(age)

def print_on_screen():
    zoo_tickets_module.clear_display()
    zoo_tickets_module.print_location("Baby....:   -", 4, 5)
    zoo_tickets_module.print_location("Kid.....:   -", 5, 5)
    zoo_tickets_module.print_location("Adult...:   -", 6, 5)
    zoo_tickets_module.print_location("Senior..:   -", 7, 5)

    zoo_tickets_module.text_format(1)
    zoo_tickets_module.print_location("Total....:", 9, 8)
    zoo_tickets_module.reset_text_format()

def data_print():
    print_on_screen()

    age = age_imput()
    total_price = 0

    while age != 0:
        ticket_type = ticket_type_identifier(age)
        ticket_price = tickets_prices[ticket_type]

        total_tickets[ticket_type] += 1

        zoo_tickets_module.print_location(total_tickets[ticket_type], \
                                          amount_of_tickets[ticket_type]['tickets_number'][0], \
                                          amount_of_tickets[ticket_type]['tickets_number'][1])

        zoo_tickets_module.print_location("{:7.2f}$".format(total_tickets[ticket_type] * ticket_price), \
                                          amount_of_tickets[ticket_type]['tickets_price'][0], \
                                          amount_of_tickets[ticket_type]['tickets_price'][1])

        total_price += ticket_price
        zoo_tickets_module.text_format(1)
        zoo_tickets_module.print_location("{:7.2f}$".format(total_price), 9, 19)
        zoo_tickets_module.reset_text_format()
        age = age_imput()

    zoo_tickets_module.locate_on_display(11, 1)

data_print()
