import zoo_tickets_module
import zoo_tickets_text_interface
from zoo_tickets_configuration import tickets_prices, amount_of_tickets

total_tickets = {
    'baby' : 0,
    'kid' : 0,
    'adult' : 0,
    'senior' : 0
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

def data_print():
    zoo_tickets_text_interface.print_on_screen()

    age = zoo_tickets_text_interface.age_imput()
    total_price = 0

    while age != 0:
        ticket_type = ticket_type_identifier(age)
        ticket_price = tickets_prices[ticket_type]

        total_tickets[ticket_type] += 1

        zoo_tickets_module.print_location(total_tickets[ticket_type], \
                                          line = amount_of_tickets[ticket_type]['tickets_number'][0], \
                                          column = amount_of_tickets[ticket_type]['tickets_number'][1])

        zoo_tickets_module.print_location("{:7.2f}$".format(total_tickets[ticket_type] * ticket_price), \
                                          line = amount_of_tickets[ticket_type]['tickets_price'][0], \
                                          column = amount_of_tickets[ticket_type]['tickets_price'][1])

        total_price += ticket_price
        zoo_tickets_module.print_location("{:7.2f}$".format(total_price), line = 9, column = 19, \
                                          style = 'bold')
        age = zoo_tickets_text_interface.age_imput()

    tickets_file = open('transactions.txt', 'a+')
    transaction = "{},{},{},{}\n".format(total_tickets['baby'], total_tickets['kid'], \
                                       total_tickets['adult'], total_tickets['senior'])
    tickets_file.write(transaction)
    tickets_file.close()

    zoo_tickets_module.locate_on_display(11, 1)

data_print()
