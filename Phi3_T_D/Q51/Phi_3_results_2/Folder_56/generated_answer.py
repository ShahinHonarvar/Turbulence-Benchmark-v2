from collections import defaultdict, Counter
from itertools import combinations

def if_contains_anagrams(string_list):
    anagram_count = 0
    for strings in combinations(string_list, 2):
        adjusted_strings = [s.lower() for s in strings]
        if all((len(c) >= 3 for c in adjusted_strings)):
            if Counter(adjusted_strings[0]) == Counter(adjusted_strings[1]):
                anagram_count += 1
    return anagram_count <= 11