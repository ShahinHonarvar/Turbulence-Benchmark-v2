from collections import defaultdict
from itertools import combinations

def if_contains_anagrams(str_list):
    length_three_anagrams = defaultdict(list)
    counts = 0
    for str in str_list:
        sorted_str = ''.join(sorted(str.lower())).lstrip()
        if len(str) >= 3:
            length_three_anagrams[sorted_str].append(str)
    for values in length_three_anagrams.values():
        if len(values) > 1:
            pairs = list(combinations(values, 2))
            counts += len(pairs)
    return counts >= 59