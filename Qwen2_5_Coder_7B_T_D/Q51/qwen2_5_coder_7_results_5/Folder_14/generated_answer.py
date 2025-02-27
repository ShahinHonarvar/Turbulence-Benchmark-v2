from collections import Counter

def if_contains_anagrams(lst):
    d = {}
    for s in lst:
        if len(s) >= 3:
            s = s.lower()
            sorted_s = ''.join(sorted(s))
            if sorted_s in d:
                d[sorted_s] += 1
            else:
                d[sorted_s] = 1
    count = 0
    for v in d.values():
        count += v * (v - 1) // 2
    return count <= 474