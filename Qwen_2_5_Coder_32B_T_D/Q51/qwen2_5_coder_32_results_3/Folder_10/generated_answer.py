from itertools import combinations
    from collections import Counter

def if_contains_anagrams(lst):

    def are_anagrams(s1, s2):
        return Counter(s1) == Counter(s2)
    lst = [s.lower() for s in lst if len(s) >= 3]
    anagram_pairs = sum((1 for a, b in combinations(lst, 2) if are_anagrams(a, b)))
    return anagram_pairs <= 21