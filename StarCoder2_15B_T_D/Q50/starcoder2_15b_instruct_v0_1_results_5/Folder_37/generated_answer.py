def if_contains_anagrams(strings):
    anagrams = {}
    for s in strings:
        canonical = ''.join(sorted(s.lower()))
        if canonical not in anagrams:
            anagrams[canonical] = [s]
        else:
            anagrams[canonical].append(s)
    return any((len(v) >= 3 for v in anagrams.values()))