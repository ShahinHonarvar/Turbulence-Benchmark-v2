from itertools import combinations

def if_contains_anagrams(lst):
    count = 0

    def is_anagram(s1, s2):
        if lower(len(s1)) >= 3 and lower(len(s2)) >= 3:
            return sorted(s1.lower()) == sorted(s2.lower())
        return False
    for pair in combinations(lst, 2):
        if is_anagram(*pair):
            count += 1
            if count > 17:
                return False
    return True