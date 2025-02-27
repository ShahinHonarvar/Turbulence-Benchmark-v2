from itertools import combinations
from string import ascii_lowercase

def is_anagram(s1, s2):
    return sorted(s1.lower()) == sorted(s2.lower())

def if_contains_anagrams(strings):
    count = 0
    for pair in combinations(strings, 2):
        if len(pair[0]) >= 3 and len(pair[1]) >= 3 and is_anagram(pair[0], pair[1]):
            count += 1
    return count <= 54