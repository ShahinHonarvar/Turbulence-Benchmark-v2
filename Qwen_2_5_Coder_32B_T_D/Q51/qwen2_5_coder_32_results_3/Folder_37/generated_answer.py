from itertools import combinations
    from collections import Counter

def if_contains_anagrams(lst):
    lst = [Counter(s.lower()) for s in lst if len(s) >= 3]
    anagram_pairs = sum((1 for a, b in combinations(lst, 2) if a == b))
    return anagram_pairs <= 206