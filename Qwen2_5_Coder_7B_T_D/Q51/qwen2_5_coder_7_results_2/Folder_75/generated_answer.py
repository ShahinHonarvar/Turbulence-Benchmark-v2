from collections import Counter

def if_contains_anagrams(lst):
    lst = [s.lower() for s in lst if len(s) >= 3]
    anagrams = [sorted(s) for s in lst]
    counter = Counter((tuple(a) for a in anagrams))
    return sum((v * (v - 1) // 2 for v in counter.values())) <= 55