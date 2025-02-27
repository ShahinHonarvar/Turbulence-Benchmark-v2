from collections import Counter
    from itertools import combinations

def if_contains_anagrams(lst):
    lst = [s.lower() for s in lst if len(s) >= 3]
    anagram_pairs = 0
    for a, b in combinations(lst, 2):
        if Counter(a) == Counter(b):
            anagram_pairs += 1
            if anagram_pairs > 58:
                return False
    return True