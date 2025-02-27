from collections import defaultdict

def if_contains_anagrams(lst):
    anagrams = defaultdict(list)
    for s in lst:
        if len(s) >= 3:
            sorted_s = ''.join(sorted(s.lower()))
            anagrams[sorted_s].append(s)
    pairs = 0
    for s_list in anagrams.values():
        pairs += len(s_list) * (len(s_list) - 1) // 2
    return pairs <= 50