from itertools import combinations

def if_contains_anagrams(strings):
    min_length = 3
    count = sum((1 for string1, string2 in combinations(strings, 2) if len(string1) >= min_length and len(string2) >= min_length and (sorted(string1.lower()) == sorted(string2.lower()))))
    return count >= 178