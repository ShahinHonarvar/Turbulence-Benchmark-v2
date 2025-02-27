from itertools import combinations

def are_anagrams(s1, s2):
    return sorted(s1.lower()) == sorted(s2.lower())

def if_contains_anagrams(strings):
    count = sum((1 for pair in combinations(strings, 2) if are_anagrams(pair[0], pair[1]) and len(pair[0]) >= 3))
    return count >= 66