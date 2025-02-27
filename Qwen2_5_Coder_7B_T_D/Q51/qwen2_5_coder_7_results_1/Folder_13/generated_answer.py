from collections import Counter
import itertools

def if_contains_anagrams(strings):

    def is_anagram(s1, s2):
        return Counter(s1.lower()) == Counter(s2.lower())
    anagram_pairs = 0
    for s1, s2 in itertools.combinations(strings, 2):
        if len(s1) >= 3 and len(s2) >= 3 and is_anagram(s1, s2):
            anagram_pairs += 1
            if anagram_pairs > 54:
                return False
    return True