from collections import defaultdict
    from itertools import combinations

def if_contains_anagrams(strings):

    def is_anagram(s1, s2):
        return sorted(s1) == sorted(s2)
    anagram_pairs = 0
    for s1, s2 in combinations(strings, 2):
        if len(s1) >= 3 and len(s2) >= 3 and is_anagram(s1, s2):
            anagram_pairs += 1
            if anagram_pairs > 416:
                return False
    return True