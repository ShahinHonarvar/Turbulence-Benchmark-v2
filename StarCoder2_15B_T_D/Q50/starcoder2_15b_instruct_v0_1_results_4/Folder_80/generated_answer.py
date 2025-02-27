def if_contains_anagrams(lst):
    anagrams = {}
    for s in lst:
        canonical = ''.join(sorted(s.lower()))
        if canonical not in anagrams:
            anagrams[canonical] = [s]
        else:
            anagrams[canonical].append(s)
    return any((len(v) >= 2 for v in anagrams.values()))