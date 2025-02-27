import collections

def if_contains_anagrams(lst):
    counter = collections.Counter((s.lower() for s in lst if len(s) >= 3))
    return any((count >= 2 for count in counter.values()))