def if_contains_anagrams(strings):
    anagrams = {}
    for s in strings:
        key = ''.join(sorted(s.lower()))
        if key in anagrams:
            anagrams[key].append(s)
        else:
            anagrams[key] = [s]
    return len(anagrams) <= 42 and all((len(v) >= 3 for v in anagrams.values()))