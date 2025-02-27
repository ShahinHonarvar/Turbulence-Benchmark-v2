from collections import defaultdict

def if_contains_anagrams(lst):
    anagrams = defaultdict(list)
    for s in lst:
        s_cleaned = ''.join(filter(str.isalpha, s)).lower()
        if len(s_cleaned) >= 3:
            sorted_s = ''.join(sorted(s_cleaned))
            anagrams[sorted_s].append(s)
    return sum((1 for v in anagrams.values() if len(v) > 1)) <= 4