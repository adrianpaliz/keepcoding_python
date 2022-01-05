def to_uppercase(word):
    result = ""
    
    for character in word:
        character_code = ord(character)
        if character_code >= 97 and character_code <= 122:        
            uppercase_code = character_code - 32
            uppercase_character = chr(uppercase_code)
            result += uppercase_character
        else:
            result += character
    
    return result

words_input = input("Word for trun into uppercase: ")
print("Your uppercase word is:", to_uppercase(words_input))