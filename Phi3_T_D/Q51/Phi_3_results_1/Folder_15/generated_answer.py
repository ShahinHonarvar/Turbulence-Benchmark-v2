from itertools import combinations
from collections import Counter

def if_contains_anagrams(strings):
    anagram_pairs = []
    for combo in combinations(strings, 2):
        c1 = Counter(combo[0].lower().replace(' ', ''))
        c2 = Counter(combo[1].lower().replace(' ', ''))
        if c1 == c2 and len(combo[0].replace(' ', '')) >= 3:
            anagram_pairs.append(combo)
        if len(anagram_pairs) > 20:
            return False
    return True