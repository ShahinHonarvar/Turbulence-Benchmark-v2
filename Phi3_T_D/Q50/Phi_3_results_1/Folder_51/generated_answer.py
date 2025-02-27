from itertools import combinations

def if_contains_anagrams(strings):
    count = 0
    for s1, s2 in combinations(strings, 2):
        if len(s1) >= 3 and s1.lower() == s2.lower()[::-1]:
            count += 1
        elif len(s2) >= 3 and s2.lower() == s1.lower()[::-1]:
            count += 1
    return count >= 39