def fahrenheit_to_celsius(range_degrees_fahrenheit):
    return (range_degrees_fahrenheit - 32) * 5 / 9

def celsius_to_fahrenheit(range_degrees_celsius):
    return (range_degrees_celsius * 9 / 5) + 32 

def celsius(start, end):
    for degrees_fahrenheit_multiples_of_ten in range(start, end + 10, 10):
        print("{} °F -> {} °C".format(degrees_fahrenheit_multiples_of_ten, round(fahrenheit_to_celsius(degrees_fahrenheit_multiples_of_ten), 2)))
        
def fahrenheit(start, end):
    for degrees_celsius_multiples_of_ten in range(start, end +10, 10):
        print("{} °C -> {} °F".format(degrees_celsius_multiples_of_ten, celsius_to_fahrenheit(degrees_celsius_multiples_of_ten)))

symbol = input("Output (F/C): ").lower()

if symbol == 'c':
    celsius(0, 230)
elif symbol == "f":
    fahrenheit(0, 100)
else:
    print("Incorrect symbol")