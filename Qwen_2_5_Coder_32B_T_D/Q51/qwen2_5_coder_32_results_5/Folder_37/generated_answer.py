from itertools import combinations
    from collections import Counter

def if_contains_anagrams(lst):
    lst = [s.lower() for s in lst if len(s) >= 3]
    anagram_count = 0
    for a, b in combinations(lst, 2):
        if Counter(a) == Counter(b):
            anagram_count += 1
    return anagram_count <= 206