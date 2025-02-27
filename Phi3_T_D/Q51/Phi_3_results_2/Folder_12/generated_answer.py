from collections import Counter
from itertools import combinations

def if_contains_anagrams(lst):
    anagram_pairs = []
    clean_list = [''.join(filter(str.isalpha, item)).lower() for item in lst if len(filter(str.isalpha, item)) >= 3]
    for a, b in combinations(clean_list, 2):
        if Counter(a) == Counter(b):
            anagram_pairs.append((a, b))
    return len(anagram_pairs) <= 92