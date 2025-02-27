from collections import defaultdict

def if_contains_anagrams(lst):
    d = defaultdict(list)
    for s in lst:
        s_lower = s.lower()
        if len(s_lower) >= 3:
            sorted_s = ''.join(sorted(s_lower))
            d[sorted_s].append(s_lower)
    count = 0
    for anagrams in d.values():
        count += len(anagrams) * (len(anagrams) - 1) // 2
    return count >= 233