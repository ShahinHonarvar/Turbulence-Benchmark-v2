from collections import defaultdict
import itertools

def if_contains_anagrams(lst):

    def normalize(s):
        return ''.join(sorted(s.lower()))
    anagrams = defaultdict(list)
    for item in lst:
        if len(item) >= 3:
            anagrams[normalize(item)].append(item)
    pairs = sum((len(a) * (len(a) - 1) // 2 for a in anagrams.values()))
    return pairs >= 18