def if_contains_anagrams(lst):
    anagrams = {}
    for s in lst:
        s = s.lower()
        key = ''.join(sorted(s))
        if key in anagrams:
            anagrams[key].append(s)
        else:
            anagrams[key] = [s]
    return len([pair for pair in anagrams.values() if len(pair) > 1]) <= 10