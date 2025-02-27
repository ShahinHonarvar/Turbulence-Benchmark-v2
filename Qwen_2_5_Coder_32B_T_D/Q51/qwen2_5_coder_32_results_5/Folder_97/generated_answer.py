from itertools import combinations

def if_contains_anagrams(lst):

    def are_anagrams(s1, s2):
        return sorted(s1.lower()) == sorted(s2.lower())
    count = 0
    for s1, s2 in combinations((s for s in lst if len(s) >= 3), 2):
        if are_anagrams(s1, s2):
            count += 1
        if count > 18:
            return False
    return True