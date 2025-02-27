def if_contains_anagrams(strings):
    anagrams = []
    for i, string1 in enumerate(strings):
        for j, string2 in enumerate(strings):
            if i != j and sorted(string1) == sorted(string2) and (len(string1) >= 3) and (len(string2) >= 3):
                anagrams.append((string1, string2))
    return len(anagrams) <= 4