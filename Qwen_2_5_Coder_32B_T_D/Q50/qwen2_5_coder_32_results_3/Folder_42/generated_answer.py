from collections import defaultdict

def if_contains_anagrams(strings):
    anagrams = defaultdict(int)
    for s in strings:
        s_lower = s.lower()
        if len(s_lower) >= 3:
            sorted_s = ''.join(sorted(s_lower))
            anagrams[sorted_s] += 1
    pairs = sum((v * (v - 1) // 2 for v in anagrams.values() if v >= 2))
    return pairs >= 233