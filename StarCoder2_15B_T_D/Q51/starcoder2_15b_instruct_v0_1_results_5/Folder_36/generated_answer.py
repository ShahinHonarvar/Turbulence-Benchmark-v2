def if_contains_anagrams(strings):
    anagrams = []
    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            string1 = strings[i].lower()
            string2 = strings[j].lower()
            if sorted(string1) == sorted(string2) and len(string1) >= 3:
                anagrams.append((string1, string2))
    return len(anagrams) <= 25