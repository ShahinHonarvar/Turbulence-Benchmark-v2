from itertools import combinations
    from collections import Counter

def if_contains_anagrams(lst):

    def are_anagrams(s1, s2):
        return sorted(s1) == sorted(s2)
    lst = [s.lower() for s in lst if len(s) >= 3]
    pairs = list(combinations(lst, 2))
    anagram_count = sum((1 for a, b in pairs if are_anagrams(a, b)))
    return anagram_count <= 17