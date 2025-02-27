def if_contains_anagrams(lst):
    anagrams = {}
    for s in lst:
        s_lower = s.lower()
        key = ''.join(sorted(s_lower))
        if key in anagrams:
            anagrams[key].append(s_lower)
        else:
            anagrams[key] = [s_lower]
    return len(list(filter(lambda x: len(x) >= 3, anagrams.values()))) <= 188