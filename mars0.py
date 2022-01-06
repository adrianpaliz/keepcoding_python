digits_16 = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f')
angle = 360 / 16
message = "alive"

for character in message:
    hexadecimal_value = hex(ord(character))
    digit_1 = hexadecimal_value[2]
    angle_1 = digits_16.index(digit_1) * angle
    
    digit_2 = hexadecimal_value[3]
    angle_2 = digits_16.index(digit_2) * angle
    
    print(digit_1, '-', angle_1)
    print(digit_2, '-', angle_2)