from collections import defaultdict

def if_contains_anagrams(lst):
    count = 0
    d = defaultdict(int)
    for s in lst:
        s = s.lower()
        if len(s) < 3:
            continue
        sorted_s = ''.join(sorted(s))
        if d[sorted_s] > 0:
            count += 1
        d[sorted_s] += 1
    return count <= 255