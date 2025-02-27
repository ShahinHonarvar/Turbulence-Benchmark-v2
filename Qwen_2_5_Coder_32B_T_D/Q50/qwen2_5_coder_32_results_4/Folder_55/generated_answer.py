from collections import defaultdict

def if_contains_anagrams(lst):
    d = defaultdict(list)
    for s in lst:
        key = ''.join(sorted(s.lower()))
        if len(s) >= 3:
            d[key].append(s)
    count = 0
    for anagrams in d.values():
        count += len(anagrams) * (len(anagrams) - 1) // 2
        if count >= 15:
            return True
    return False