def is_decimal(number):
    try:
        float(number)
        return True
    except:
        return False
    
input_base = input("Triangle base: ")
if is_decimal(input_base):
    base = float(input_base)
else:
    print(input_base, "must be a number")
    quit()
    
input_height = input("Triangle height: ")
if is_decimal(input_height):
    height = float(input_height)
else:
    print(input_height, "must be a number")
    quit()

height = float(input_height)

area = base * height / 2

print("Triangle surface: ", round(area, 2))