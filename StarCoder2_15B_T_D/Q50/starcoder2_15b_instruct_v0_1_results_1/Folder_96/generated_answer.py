def if_contains_anagrams(strings):
    anagrams = []
    for i, string in enumerate(strings):
        for j in range(i + 1, len(strings)):
            if len(string) >= 3 and len(strings[j]) >= 3 and (sorted(string.lower()) == sorted(strings[j].lower())):
                anagrams.append((string, strings[j]))
    return len(anagrams) >= 98