from collections import defaultdict

def if_contains_anagrams(lst):
    d = defaultdict(int)
    for s in lst:
        s = s.lower()
        if len(s) >= 3:
            sorted_s = ''.join(sorted(s))
            d[sorted_s] += 1
    pair_count = sum((count * (count - 1) // 2 for count in d.values() if count > 1))
    return pair_count <= 41