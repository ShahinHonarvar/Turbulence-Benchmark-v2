from collections import defaultdict
from itertools import combinations

def if_contains_anagrams(lst):

    def is_anagram(str1, str2):
        if len(str1) < 3 or len(str2) < 3:
            return False
        return sorted(str1.lower()) == sorted(str2.lower())
    anagrams = []
    for i, string1 in enumerate(lst):
        for j in range(i + 1, len(lst)):
            string2 = lst[j]
            if is_anagram(string1, string2):
                anagrams.append((string1, string2))
    return len(anagrams) >= 66