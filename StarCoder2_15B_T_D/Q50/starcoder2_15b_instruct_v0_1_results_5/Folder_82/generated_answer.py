def if_contains_anagrams(strings):
    anagrams = set()
    for i, string in enumerate(strings):
        for j in range(i + 1, len(strings)):
            if sorted(string.lower()) == sorted(strings[j].lower()):
                anagrams.add((string, strings[j]))
    return len(anagrams) >= 276