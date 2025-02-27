from collections import defaultdict

def if_contains_anagrams(lst):
    s = defaultdict(int)
    for i in lst:
        w = ''.join(sorted(i.lower()))
        if len(w) >= 3:
            s[w] += 1
    c = 0
    for v in s.values():
        c += v * (v - 1) // 2
    return c >= 50