from collections import defaultdict

def if_contains_anagrams(lst):
    anagrams = defaultdict(list)
    for s in lst:
        s = s.lower()
        if len(s) >= 3:
            sorted_s = ''.join(sorted(s))
            anagrams[sorted_s].append(s)
    for group in anagrams.values():
        if len(group) > 1:
            if len(group) * (len(group) - 1) // 2 >= 35:
                return True
    return False