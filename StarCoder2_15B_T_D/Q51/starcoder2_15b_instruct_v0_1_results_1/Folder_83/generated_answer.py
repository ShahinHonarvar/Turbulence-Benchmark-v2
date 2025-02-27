def if_contains_anagrams(list_of_strings):
    anagrams = 0
    for string1 in list_of_strings:
        for string2 in list_of_strings:
            if sorted(string1.lower()) == sorted(string2.lower()) and len(string1) >= 3:
                anagrams += 1
                break
    return anagrams <= 19