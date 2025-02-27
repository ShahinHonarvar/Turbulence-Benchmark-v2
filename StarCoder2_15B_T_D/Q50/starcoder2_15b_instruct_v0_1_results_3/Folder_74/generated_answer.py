def if_contains_anagrams(strings):
    anagrams = {}
    for s in strings:
        key = ''.join(sorted(s.lower()))
        if key not in anagrams:
            anagrams[key] = [s]
        else:
            anagrams[key].append(s)
    return any((len(v) >= 17 for v in anagrams.values()))