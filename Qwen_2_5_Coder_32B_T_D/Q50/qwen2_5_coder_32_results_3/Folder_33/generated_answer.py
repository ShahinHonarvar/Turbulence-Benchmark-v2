from collections import defaultdict

def if_contains_anagrams(lst):
    d = defaultdict(list)
    for s in lst:
        s_lower = s.lower()
        if len(s_lower) >= 3:
            d[''.join(sorted(s_lower))].append(s_lower)
    count = 0
    for anagrams in d.values():
        if len(anagrams) > 1:
            count += len(anagrams) * (len(anagrams) - 1) // 2
    return count >= 140