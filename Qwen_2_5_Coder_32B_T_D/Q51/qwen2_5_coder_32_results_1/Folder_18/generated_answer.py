from itertools import combinations

def if_contains_anagrams(lst):

    def are_anagrams(s1, s2):
        return sorted(s1.lower()) == sorted(s2.lower())
    count = 0
    for a, b in combinations(lst, 2):
        if len(a) >= 3 and len(b) >= 3 and are_anagrams(a, b):
            count += 1
            if count > 42:
                return False
    return True