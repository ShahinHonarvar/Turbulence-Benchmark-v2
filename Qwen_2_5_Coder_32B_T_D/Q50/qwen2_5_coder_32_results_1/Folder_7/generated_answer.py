from itertools import combinations
    from collections import Counter

def if_contains_anagrams(lst):

    def is_anagram(s1, s2):
        return Counter(s1.lower()) == Counter(s2.lower())
    anagram_pairs = 0
    valid_combinations = combinations((s for s in lst if len(s) >= 3), 2)
    for s1, s2 in valid_combinations:
        if is_anagram(s1, s2):
            anagram_pairs += 1
            if anagram_pairs >= 178:
                return True
    return False