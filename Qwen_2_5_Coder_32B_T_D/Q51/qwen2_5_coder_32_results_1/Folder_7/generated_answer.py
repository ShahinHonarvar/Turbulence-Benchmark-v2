from itertools import combinations

def if_contains_anagrams(lst):

    def are_anagrams(s1, s2):
        return sorted(s1.lower()) == sorted(s2.lower())
    count = 0
    for s1, s2 in combinations(lst, 2):
        if len(s1) >= 3 and len(s2) >= 3 and are_anagrams(s1, s2):
            count += 1
            if count > 445:
                return False
    return True