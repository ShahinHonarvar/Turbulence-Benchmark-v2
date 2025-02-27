def if_contains_anagrams(strings):
    filtered = [''.join(sorted(s.lower())) for s in strings if len(s) >= 3]
    anagrams = {}
    for word in filtered:
        anagrams.setdefault(word, []).append(word)
    return sum((len(lst) > 1 for lst in anagrams.values())) >= 25