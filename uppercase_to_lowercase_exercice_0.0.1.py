def to_lowercase(word):
    result = ""
    
    for character in word:
        character_code = ord(character)
        if character_code >= 65 and character_code <= 90:
            lowercase_code = character_code + 32
            lowercase_character = chr(lowercase_code)
            result += lowercase_character
        else:
            result += character

    return result

words_input = input("Word for trun into lowercase: ")
print("Your lowercase word is:", to_lowercase(words_input))