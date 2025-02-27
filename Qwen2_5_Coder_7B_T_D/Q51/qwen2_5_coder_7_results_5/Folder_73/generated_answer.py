def if_contains_anagrams(lst):

    def normalize(s):
        return ''.join(sorted(s.lower()))
    anagrams = {}
    for s in lst:
        if len(s) >= 3:
            normalized = normalize(s)
            if normalized in anagrams:
                anagrams[normalized].append(s)
            else:
                anagrams[normalized] = [s]
    pairs = 0
    for group in anagrams.values():
        n = len(group)
        pairs += n * (n - 1) // 2
    return pairs <= 279