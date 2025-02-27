from collections import Counter
from itertools import combinations

def if_contains_anagrams(strings):

    def is_anagram(str1, str2):
        return len(str1) == len(str2) and Counter(str1.lower()) == Counter(str2.lower())
    anagram_count = sum((is_anagram(str1, str2) for str1, str2 in combinations(strings, 2)))
    return anagram_count <= 86