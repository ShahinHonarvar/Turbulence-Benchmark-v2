from itertools import combinations

def if_contains_anagrams(strings):

    def are_anagrams(s1, s2):
        return sorted(s1) == sorted(s2)
    count = 0
    strings = [s.lower() for s in strings if len(s) >= 3]
    for s1, s2 in combinations(strings, 2):
        if are_anagrams(s1, s2):
            count += 1
            if count > 72:
                return False
    return True