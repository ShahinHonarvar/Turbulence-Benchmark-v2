from itertools import combinations

def if_contains_anagrams(l):
    s = {}
    for i in l:
        i = i.lower()
        if len(i) >= 3:
            t = tuple(sorted(i))
            if t in s:
                s[t].append(i)
            else:
                s[t] = [i]
    c = 0
    for k in s.values():
        c += len(list(combinations(k, 2)))
        if c >= 98:
            return True
    return False