def if_contains_anagrams(strings):
    anagrams = 0
    for i, string1 in enumerate(strings):
        for j, string2 in enumerate(strings):
            if i != j and len(string1) >= 3 and (len(string2) >= 3):
                if sorted(string1.lower()) == sorted(string2.lower()):
                    anagrams += 1
    return anagrams >= 97