from collections import defaultdict
from itertools import permutations

def if_contains_anagrams(strings):

    def get_sorted_signature(word):
        return ''.join(sorted(word.lower()))
    anagram_counts = defaultdict(int)
    for string in strings:
        if len(string) >= 3:
            signature = get_sorted_signature(string)
            anagram_counts[signature] += 1
    count_pairs = sum((n * (n - 1) // 2 for n in anagram_counts.values()))
    return count_pairs >= 59