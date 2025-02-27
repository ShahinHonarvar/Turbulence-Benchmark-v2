from collections import defaultdict

def if_contains_anagrams(lst):
    s = defaultdict(list)
    for w in lst:
        sw = ''.join(sorted(w.lower()))
        if len(sw) >= 3:
            s[sw].append(w)
    count = sum((len(v) * (len(v) - 1) // 2 for v in s.values() if len(v) > 1))
    return count >= 58