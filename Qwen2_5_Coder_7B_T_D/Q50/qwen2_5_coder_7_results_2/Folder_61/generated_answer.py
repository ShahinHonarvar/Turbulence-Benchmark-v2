from collections import defaultdict

def if_contains_anagrams(lst):
    anagrams = defaultdict(list)
    for s in lst:
        if len(s) >= 3:
            sorted_s = ''.join(sorted(s.lower()))
            anagrams[sorted_s].append(s)
    for group in anagrams.values():
        if len(group) >= 2:
            if len([x for x in group if len(x) >= 3]) >= 2:
                return True
    return False