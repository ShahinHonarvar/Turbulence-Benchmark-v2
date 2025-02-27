from itertools import combinations
    from collections import Counter

def if_contains_anagrams(lst):

    def is_anagram(s1, s2):
        return Counter(s1) == Counter(s2)
    lst = [s.lower() for s in lst if len(s) >= 3]
    anagram_pairs = sum((is_anagram(s1, s2) for s1, s2 in combinations(lst, 2)))
    return anagram_pairs <= 474