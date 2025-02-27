def if_contains_anagrams(strings):
    anagrams = []
    for i, string1 in enumerate(strings):
        for j, string2 in enumerate(strings):
            if i != j and len(string1) >= 3 and (len(string2) >= 3) and (sorted(string1.lower()) == sorted(string2.lower())):
                anagrams.append(string1)
                break
    return len(anagrams) >= 77