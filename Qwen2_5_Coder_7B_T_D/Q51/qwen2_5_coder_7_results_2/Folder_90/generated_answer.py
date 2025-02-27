def if_contains_anagrams(strings):
    anagrams = {}
    for s in strings:
        s = s.lower()
        if len(s) >= 3:
            sorted_s = ''.join(sorted(s))
            if sorted_s in anagrams:
                anagrams[sorted_s].append(s)
            else:
                anagrams[sorted_s] = [s]
    pairs = 0
    for key, value in anagrams.items():
        if len(value) > 1:
            pairs += len(value) * (len(value) - 1) // 2
    return pairs <= 147