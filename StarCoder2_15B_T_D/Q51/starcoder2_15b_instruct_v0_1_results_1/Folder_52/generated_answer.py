def if_contains_anagrams(strings):
    anagrams = {}
    for s in strings:
        s = s.lower()
        s = ''.join((c for c in s if c.isalpha()))
        if len(s) >= 3:
            s_sorted = ''.join(sorted(s))
            if s_sorted in anagrams:
                anagrams[s_sorted].append(s)
            else:
                anagrams[s_sorted] = [s]
    num_anagrams = sum((len(v) - 1 for v in anagrams.values()))
    return num_anagrams <= 43