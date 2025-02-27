from collections import defaultdict

def if_contains_anagrams(strings):
    anagrams = defaultdict(list)
    for s in strings:
        lower_s = s.lower()
        if len(lower_s) >= 3:
            sorted_s = tuple(sorted(lower_s))
            anagrams[sorted_s].append(lower_s)
    pairs = sum((len(v) * (len(v) - 1) // 2 for v in anagrams.values() if len(v) > 1))
    return pairs >= 8