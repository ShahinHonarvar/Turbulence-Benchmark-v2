from collections import defaultdict
import itertools

def if_contains_anagrams(strings):
    sorted_strings = [''.join(sorted(s.lower())) for s in strings if len(s) >= 3]
    anagram_count = defaultdict(int)
    for s in sorted_strings:
        anagram_count[s] += 1
        if anagram_count[s] > 1:
            return True
    return len(list(filter(lambda x: x > 1, anagram_count.values()))) <= 36