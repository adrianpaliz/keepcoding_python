message = "61 6c 69 76 65"
hexadecimal_string = message
bytes_object = bytes.fromhex(hexadecimal_string)
ascii_string = bytes_object.decode()
print(ascii_string)
