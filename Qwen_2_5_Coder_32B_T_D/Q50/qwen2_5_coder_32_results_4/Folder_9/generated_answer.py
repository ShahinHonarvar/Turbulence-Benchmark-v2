from itertools import combinations
    from collections import Counter

def if_contains_anagrams(strings):

    def are_anagrams(s1, s2):
        return Counter(s1) == Counter(s2)
    count = 0
    strings = [s.lower() for s in strings if len(s) >= 3]
    for s1, s2 in combinations(strings, 2):
        if are_anagrams(s1, s2):
            count += 1
            if count >= 66:
                return True
    return False