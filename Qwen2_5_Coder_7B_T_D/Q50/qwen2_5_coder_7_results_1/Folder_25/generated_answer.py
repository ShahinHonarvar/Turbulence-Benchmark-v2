from collections import defaultdict
    from itertools import combinations

def if_contains_anagrams(lst):

    def is_anagram(s1, s2):
        return sorted(s1.lower()) == sorted(s2.lower())
    anagram_pairs = set()
    for s1, s2 in combinations(lst, 2):
        if len(s1) >= 3 and len(s2) >= 3 and is_anagram(s1, s2):
            pair = tuple(sorted([s1, s2]))
            if pair not in anagram_pairs:
                anagram_pairs.add(pair)
    return len(anagram_pairs) >= 14