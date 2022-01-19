import click
colors = {
    'black' : '30',
    'red' : '31',
    'green' : '32',
    'yellow' : '33',
    'blue' : '34',
    'magenta' : '35',
    'cyan' : '36',
    'while' : '37',
    'reset' : '39'    
    }

background = {
    'black' : '40',
    'red' : '41',
    'green' : '42',
    'yellow' : '43',
    'blue' : '44',
    'magenta' : '45',
    'cyan' : '46',
    'while' : '47',
    'reset' : '49'   
    }

styles = {
    'bold' : 1,
    'underline' : 4,
    'blink' : 5,
    'reversed' : 7    
    }


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
    
def process_parameters(parameters):
    if 'line' in parameters:
        line = parameters['line']
        column = 1
        if 'column' in parameters:
            column = parameters['column']
        locate_on_display(line, column)
    
    if 'color' in parameters and parameters['color'] in colors:
        print("\033[{}m".format(colors[parameters['color']]), end ="")
    
    if 'background' in parameters and parameters['background'] in background:
        print("\033[{}m".format(background[parameters['background']]), end ="")
    
    if 'style' in parameters and parameters['style'] in styles:
        print("\033[{}m".format(styles[parameters['style']]), end ="")        
    

def print_location(string, **parameters):
    process_parameters(parameters)
    if 'new_line' in parameters and parameters['new_line']:
        print(string)
    else:
        print(string, end="")
    
    if 'new_return' not in parameters:
        reset_text_format()    
    
def input_location(message, **parameters):
    process_parameters(parameters)
    if 'data' not in parameters:
        clear_line()
    return input(message)
    
def text_format(style, text_color = 'white', background_color = 'black'):
    click.style
    
def reset_text_format():
    print("\033[0m", end = "")