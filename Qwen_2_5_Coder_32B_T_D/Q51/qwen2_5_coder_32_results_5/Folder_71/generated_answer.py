from collections import defaultdict

def if_contains_anagrams(s):
    a = defaultdict(list)
    for w in s:
        w = w.lower()
        if len(w) >= 3:
            a[''.join(sorted(w))].append(w)
    c = sum((1 for v in a.values() if len(v) > 1))
    return c <= 9