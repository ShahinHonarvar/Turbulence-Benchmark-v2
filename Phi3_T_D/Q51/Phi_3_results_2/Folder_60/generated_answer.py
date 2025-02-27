from collections import defaultdict
from itertools import combinations

def if_contains_anagrams(strings):
    anagram_buckets = defaultdict(list)
    for s in strings:
        sorted_s = ''.join(sorted(s.lower()))
        anagram_buckets[sorted_s].append(s)
    count = 0
    for anagrams in anagram_buckets.values():
        if len(anagrams) > 1 and len(anagrams) >= 3:
            count += sum((1 for pair in combinations(anagrams, 2)))
    return count <= 77