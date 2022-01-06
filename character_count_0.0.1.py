sentence = "Real change, enduring change, happens one step at a time." # Quote by Ruth Bader Ginsburg

frequencies = dict()

for character in sentence:
    if character in frequencies:
        frequencies[character] += 1
    else:
        frequencies[character] = 1
        
for letter in frequencies.keys():
    print(letter, "-", frequencies[letter])