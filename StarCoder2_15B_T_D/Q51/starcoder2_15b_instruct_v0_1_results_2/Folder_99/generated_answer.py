def if_contains_anagrams(strings):
    anagrams = {}
    for s in strings:
        s = s.lower()
        if s in anagrams:
            anagrams[s] += 1
        else:
            anagrams[s] = 1
    return sum((v > 1 for v in anagrams.values())) <= 93