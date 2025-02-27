from collections import defaultdict
from itertools import combinations

def if_contains_anagrams(strings):

    def str_signature(s):
        lowered = s.lower()
        return ''.join(sorted(filter(str.isalpha, lowered)))
    anagram_counts = defaultdict(int)
    for string in strings:
        if len(string) >= 3:
            signature = str_signature(string)
            anagram_counts[signature] += 1
    return sum((1 for count in anagram_counts.values() if count > 1)) <= 445