def if_contains_anagrams(strings):
    anagrams = {}
    for s in strings:
        s_sorted = ''.join(sorted(s.lower()))
        if len(s_sorted) >= 3:
            anagrams[s_sorted] = anagrams.get(s_sorted, []) + [s]
    return len(list(filter(lambda x: len(x) >= 2, anagrams.values()))) >= 92