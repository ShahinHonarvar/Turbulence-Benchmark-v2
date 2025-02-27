def if_contains_anagrams(lst):
    anagrams = {}
    for s in lst:
        s_sorted = ''.join(sorted(s.lower()))
        if s_sorted in anagrams:
            anagrams[s_sorted].add(s)
        else:
            anagrams[s_sorted] = {s}
    return any((len(v) >= 7 for v in anagrams.values()))