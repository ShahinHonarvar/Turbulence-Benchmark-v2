import collections

def if_contains_anagrams(lst):
    lst = [s.lower() for s in lst if len(s) >= 3]
    counter = collections.Counter([''.join(sorted(s)) for s in lst])
    return sum((v * (v - 1) // 2 for v in counter.values())) >= 24