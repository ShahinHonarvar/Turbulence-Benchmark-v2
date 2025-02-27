from collections import Counter
    from itertools import combinations

def if_contains_anagrams(lst):

    def is_anagram(s1, s2):
        return Counter(s1.lower()) == Counter(s2.lower())
    return sum((is_anagram(a, b) for a, b in combinations(lst, 2))) <= 464