from collections import defaultdict

def if_contains_anagrams(strings):
    count = defaultdict(int)
    for s in strings:
        s = s.lower()
        if len(s) >= 3:
            sorted_s = tuple(sorted(s))
            count[sorted_s] += 1
    pairs = sum((v * (v - 1) // 2 for v in count.values() if v > 1))
    return pairs >= 155