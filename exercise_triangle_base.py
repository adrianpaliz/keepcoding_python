def is_decimal(number):
    try:
        float(number)
        return True
    except:
        return False
    
input_base = input("Triangle base: ")
while not is_decimal(input_base):
    print(input_base, "must be a number")
    input_base = input("Triangle base: ")
    
input_height = input("Triangle height: ")
while not is_decimal(input_height):
    print(input_height, "must be a number")
    input_height = input("Triangle height: ")

base = float(input_base)
height = float(input_height)
area = base * height / 2

print("Triangle surface: ", round(area, 2))