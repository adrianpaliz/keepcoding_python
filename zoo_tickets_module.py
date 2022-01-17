def clear_display():
    print("\033[2J")

def locate_on_display(line, column):
    print("\033[{};{}H".format(line, column), end = "")

def clear_line(line = None, column = None):
    if line is not None and column is not None:
        locate_on_display(line, column)
    elif line is not None:
        locate_on_display(line, 1)
        
    print("\033[K", end = "")

def print_location(string, line, column, delete_end = False):
    locate_on_display(line, column)
    if delete_end:
        clear_line()
    print(string, end = "")
    
def input_location(string, line, column, delete_end = True):
    locate_on_display(line, column)
    if delete_end:
        clear_line()
    return input(string)

def text_format(text_style, text_color = 37, background_color = 40):
    print("\033[{};{};{}m".format(text_style, text_color, background_color), end = "")
    
def reset_text_format():
    text_format(0, 37, 40)