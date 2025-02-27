from collections import defaultdict
from itertools import permutations

def if_contains_anagrams(strings):
    sorted_strings = [''.join(sorted(s.lower())) for s in strings if len(s) >= 3]
    anagram_counts = defaultdict(int)
    for s in sorted_strings:
        anagram_counts[s] += 1
    return sum((count * (count - 1) // 2 for count in anagram_counts.values())) >= 246