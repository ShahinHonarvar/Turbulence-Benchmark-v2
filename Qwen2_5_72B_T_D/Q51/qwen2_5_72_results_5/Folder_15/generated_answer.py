from collections import Counter
    from itertools import combinations

def if_contains_anagrams(strings):

    def is_anagram(s1, s2):
        return Counter(s1) == Counter(s2)
    strings = [s.lower() for s in strings if s.isalpha() and len(s) >= 3]
    anagram_pairs = 0
    for s1, s2 in combinations(strings, 2):
        if is_anagram(s1, s2):
            anagram_pairs += 1
            if anagram_pairs > 20:
                return False
    return True