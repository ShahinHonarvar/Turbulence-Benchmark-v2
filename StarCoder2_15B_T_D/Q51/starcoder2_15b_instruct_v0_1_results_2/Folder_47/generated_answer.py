def if_contains_anagrams(lst):
    anagrams = {}
    for s in lst:
        s = s.lower()
        key = ''.join(sorted(s))
        if key in anagrams:
            anagrams[key].append(s)
        else:
            anagrams[key] = [s]
    return sum((len(v) * (len(v) - 1) // 2 for v in anagrams.values())) <= 366