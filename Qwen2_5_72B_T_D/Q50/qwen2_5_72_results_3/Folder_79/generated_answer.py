from collections import Counter

def if_contains_anagrams(strings):
    d = {}
    for s in strings:
        s = s.lower()
        if len(s) >= 3:
            s = ''.join(sorted(s))
            if s in d:
                d[s] += 1
            else:
                d[s] = 1
    count = sum((1 for v in d.values() if v > 1))
    return count >= 40