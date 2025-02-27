from collections import defaultdict
from itertools import combinations

def if_contains_anagrams(strings):

    def are_anagrams(s1, s2):
        return sorted(s1.lower()) == sorted(s2.lower()) and len(s1) >= 3
    anagrams_count = 0
    for string1, string2 in combinations(strings, 2):
        if are_anagrams(string1, string2):
            anagrams_count += 1
    return anagrams_count <= 392