from collections import defaultdict

def if_contains_anagrams(strings):
    count = defaultdict(int)
    for s in strings:
        s = s.lower()
        if len(s) >= 3:
            s = ''.join(sorted(s))
            count[s] += 1
    pairs = sum((v * (v - 1) // 2 for v in count.values()))
    return pairs >= 312