from collections import defaultdict
import itertools

def if_contains_anagrams(words):
    anagram_counts = defaultdict(int)
    for word in words:
        if len(word) >= 3:
            sorted_tuple = tuple(sorted(word.lower()))
            anagram_counts[sorted_tuple] += 1
    num_anagram_pairs = sum((count * (count - 1) // 2 for count in anagram_counts.values()))
    return num_anagram_pairs >= 123