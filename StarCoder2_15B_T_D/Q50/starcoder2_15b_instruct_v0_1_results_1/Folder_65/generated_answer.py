def if_contains_anagrams(lst):
    anagrams = {}
    for s in lst:
        s_sorted = ''.join(sorted(s.lower()))
        if s_sorted in anagrams:
            anagrams[s_sorted].append(s)
        else:
            anagrams[s_sorted] = [s]
    count = 0
    for v in anagrams.values():
        n = len(v)
        count += n * (n - 1) // 2
    return count >= 94