def if_contains_anagrams(list_of_strings):
    anagrams = 0
    for i in range(len(list_of_strings)):
        for j in range(i + 1, len(list_of_strings)):
            if sorted(list_of_strings[i].lower()) == sorted(list_of_strings[j].lower()) and len(list_of_strings[i]) >= 3 and (len(list_of_strings[j]) >= 3):
                anagrams += 1
                if anagrams > 475:
                    return False
    return anagrams <= 475