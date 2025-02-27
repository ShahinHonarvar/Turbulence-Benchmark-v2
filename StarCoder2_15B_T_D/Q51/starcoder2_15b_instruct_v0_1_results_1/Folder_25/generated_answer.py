import re
from itertools import combinations
from collections import Counter

def if_contains_anagrams(strings):
    pattern = re.compile('^[a-z]{3,}$')
    anagram_pairs = 0
    for s1, s2 in combinations(strings, 2):
        if pattern.match(s1) and pattern.match(s2) and (Counter(s1) == Counter(s2)):
            anagram_pairs += 1
            if anagram_pairs > 67:
                return False
    return anagram_pairs <= 67