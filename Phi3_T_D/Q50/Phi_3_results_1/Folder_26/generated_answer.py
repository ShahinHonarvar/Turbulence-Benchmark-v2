from collections import defaultdict
from itertools import combinations

def if_contains_anagrams(strings):
    anagram_counts = defaultdict(int)
    for string in strings:
        sorted_str = ''.join(sorted(string.lower()))
        anagram_counts[sorted_str] += 1
    anagram_pairs = sum((1 for count in anagram_counts.values() if count >= 2))
    return anagram_pairs // 2 >= 49