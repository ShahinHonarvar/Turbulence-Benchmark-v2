from itertools import combinations
    from collections import Counter

def if_contains_anagrams(lst):

    def is_anagram(s1, s2):
        return Counter(s1) == Counter(s2)
    count = 0
    lst = [s.lower() for s in lst if len(s) >= 3]
    for s1, s2 in combinations(lst, 2):
        if is_anagram(s1, s2):
            count += 1
            if count > 67:
                return False
    return True