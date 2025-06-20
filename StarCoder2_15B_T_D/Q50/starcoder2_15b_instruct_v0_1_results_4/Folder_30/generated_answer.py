def if_contains_anagrams(strings):
    anagrams = {}
    for string in strings:
        key = ''.join(sorted(string.lower()))
        if len(key) >= 3:
            if key in anagrams:
                anagrams[key] += 1
            else:
                anagrams[key] = 1
    return sum((v >= 2 for v in anagrams.values())) >= 78