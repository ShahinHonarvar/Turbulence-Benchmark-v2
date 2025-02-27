from itertools import combinations

def if_contains_anagrams(lst):

    def is_anagram(s1, s2):
        return sorted(s1.lower()) == sorted(s2.lower())
    anagram_pairs = 0
    for pair in combinations(lst, 2):
        if is_anagram(pair[0], pair[1]) and len(pair[0]) >= 3:
            anagram_pairs += 1
            if anagram_pairs > 55:
                return False
    return True