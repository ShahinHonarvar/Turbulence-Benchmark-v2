from collections import defaultdict
from itertools import combinations

def build_key(s):
    return ''.join(sorted(s.lower()))

def if_contains_anagrams(lst):
    d = defaultdict(int)
    for word in lst:
        if len(word) >= 3:
            key = build_key(word)
            d[key] += 1
    num_anagrams = sum((count * (count - 1) // 2 for count in d.values() if count > 1))
    return num_anagrams >= 143