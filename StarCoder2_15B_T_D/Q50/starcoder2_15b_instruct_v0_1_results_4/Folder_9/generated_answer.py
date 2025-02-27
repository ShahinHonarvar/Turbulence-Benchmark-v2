def if_contains_anagrams(strings):
    anagrams = {}
    for s in strings:
        key = ''.join(sorted(s.lower()))
        if len(key) >= 3:
            anagrams[key] = anagrams.get(key, []) + [s]
    return any((len(v) >= 2 for v in anagrams.values()))