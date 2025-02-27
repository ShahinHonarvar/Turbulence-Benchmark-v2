from collections import defaultdict

def if_contains_anagrams(lst):
    d = defaultdict(int)
    for s in lst:
        s = s.lower()
        if len(s) >= 3:
            sorted_s = ''.join(sorted(s))
            d[sorted_s] += 1
    count = 0
    for key in d:
        count += d[key] * (d[key] - 1) // 2
        if count > 21:
            return False
    return True