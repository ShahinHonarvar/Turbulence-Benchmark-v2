from collections import Counter
    from itertools import combinations

def if_contains_anagrams(lst):
    lst = [s.lower() for s in lst if len(s) >= 3]
    anagram_pairs = 0
    for s1, s2 in combinations(lst, 2):
        if Counter(s1) == Counter(s2):
            anagram_pairs += 1
            if anagram_pairs > 210:
                return False
    return True