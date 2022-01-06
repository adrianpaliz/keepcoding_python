def exists(letter, table):
    position = 0
    while position < len(table):
        if table[position] == letter:
            return position
        position += 1
    
    return None

sentence = "Real change, enduring change, happens one step at a time." # Quote by Ruth Bader Ginsburg

letters = []
frequencies = []

for character in sentence:
    position = exists(character, letters)
    if position != None:
        frequencies[position] += 1
    else:
        letters.append(character)
        frequencies.append(1)

index = 0
while index < len(letters):
    print(letters[index], "-", frequencies[index])
    index += 1