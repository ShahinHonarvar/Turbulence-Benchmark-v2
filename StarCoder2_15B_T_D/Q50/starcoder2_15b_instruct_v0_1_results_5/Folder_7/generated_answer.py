def if_contains_anagrams(strings):
    anagrams = {}
    for s in strings:
        s_sorted = ''.join(sorted(s.lower()))
        if s_sorted in anagrams:
            anagrams[s_sorted].append(s)
        else:
            anagrams[s_sorted] = [s]
    return sum((len(v) for v in anagrams.values())) >= 178