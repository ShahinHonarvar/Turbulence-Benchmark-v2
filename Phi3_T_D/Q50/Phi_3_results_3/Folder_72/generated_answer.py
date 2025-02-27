from collections import defaultdict
import itertools 

def if_contains_anagrams(strings):
    sorted_dict = defaultdict(list)
    anagram_pairs_count = 0
    for s in strings:
        if len(s) >= 3:
            sorted_tuple = tuple(sorted(s.lower()))
            sorted_dict[sorted_tuple].append(s)
    for values in sorted_dict.values():
        if len(values) > 1:
            anagram_pairs_count += len(list(itertools.combinations(values, 2)))
    return anagram_pairs_count >= 55