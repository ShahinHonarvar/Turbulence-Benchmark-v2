from collections import Counter

def if_contains_anagrams(l):
    seen = Counter()
    for s in l:
        s = ''.join(sorted(s.lower()))
        if len(s) >= 3:
            seen[s] += 1
    return sum((v * (v - 1) // 2 for v in seen.values())) <= 257