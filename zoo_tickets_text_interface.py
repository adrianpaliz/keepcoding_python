import zoo_tickets_module

def age_imput_validation(raw_input):
    try:
        integer = int(raw_input)
        if integer >= 0:
            return True
        return False
    except:
        return False

def age_imput():
    age = zoo_tickets_module.input_location("How old you are?: ", line = 1, column = 1)
    while age_imput_validation(age) == False:
        zoo_tickets_module.print_location("Wrong age", line = 25, column = 1, style = 'bold', color = 'yellow', background = 'red')
        age = zoo_tickets_module.input_location("How old you are?: ", line = 1, column = 1)

    zoo_tickets_module.clear_line(25)

    return int(age)

def print_on_screen():
    zoo_tickets_module.clear_display()
    zoo_tickets_module.print_location("Baby....:   -", line = 4, column = 5)
    zoo_tickets_module.print_location("Kid.....:   -", line = 5, column = 5)
    zoo_tickets_module.print_location("Adult...:   -", line = 6, column = 5)
    zoo_tickets_module.print_location("Senior..:   -", line = 7, column = 5)

    zoo_tickets_module.text_format(1)
    zoo_tickets_module.print_location("Total....:", line = 9, column = 8)
    zoo_tickets_module.reset_text_format()