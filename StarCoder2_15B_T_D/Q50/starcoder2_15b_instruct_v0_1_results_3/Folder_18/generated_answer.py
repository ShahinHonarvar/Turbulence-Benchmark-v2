def if_contains_anagrams(strings):
    anagrams = set()
    for string1 in strings:
        for string2 in strings:
            if string1.lower() != string2.lower() and len(string1) >= 3 and (len(string2) >= 3) and (sorted(string1.lower()) == sorted(string2.lower())):
                anagrams.add((string1, string2))
    return len(anagrams) >= 10 ** 6