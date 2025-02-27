from collections import defaultdict

def if_contains_anagrams(lst):
    anagrams = defaultdict(int)
    for s in lst:
        sorted_s = ''.join(sorted(s.lower()))
        if len(sorted_s) >= 3:
            anagrams[sorted_s] += 1
    pairs_of_anagrams = sum((x * (x - 1) // 2 for x in anagrams.values()))
    return pairs_of_anagrams <= 9