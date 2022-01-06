message = "alive"

for character in message:
    hexadecimal_value = hex(ord(character))
    digit_1 = hexadecimal_value[2]
    digit_2 = hexadecimal_value[3]

    print(digit_1)
    print(digit_2)
