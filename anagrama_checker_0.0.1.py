def is_anagram(word_1, word_2):
    letters_comparison = []

    if len(word_1) != len(word_2):
        return False

    for character_1 in word_1:
        do_not_add_false = False
        for character_2 in word_2:
            if character_1 == character_2:
                do_not_add_false = True
                letters_comparison.append(True)

        if not do_not_add_false:
            letters_comparison.append(False)

    if False in letters_comparison:
        return False
    else:
        return True
