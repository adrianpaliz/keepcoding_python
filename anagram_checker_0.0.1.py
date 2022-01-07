def character_count(chain):
    result= dict()

    for character in chain:
        if character in result:
            result[character] += 1
        else:
            result[character] = 1

    return result

def is_anagram(word_1, word_2):
    dictionary_word_1 = character_count(word_1)
    dictionary_word_2 = character_count(word_2)

    if len(dictionary_word_1) != len(dictionary_word_2):
        return False

    for character in dictionary_word_1:
        if character in dictionary_word_2 and dictionary_word_1[character] == dictionary_word_2[character]:
            pass
        else:
            return False

    return True
