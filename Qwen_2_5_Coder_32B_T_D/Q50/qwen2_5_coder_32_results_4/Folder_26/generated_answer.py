from collections import defaultdict

def if_contains_anagrams(strings):
    count = defaultdict(int)
    for s in strings:
        if len(s) >= 3:
            s = s.lower()
            s = ''.join(sorted(s))
            count[s] += 1
    pairs = sum((c * (c - 1) // 2 for c in count.values() if c > 1))
    return pairs >= 49