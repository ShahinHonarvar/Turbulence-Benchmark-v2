from itertools import combinations

def if_contains_anagrams(lst):

    def normalize(s):
        return sorted(filter(str.isalpha, s.lower()))

    def is_anagram(s1, s2):
        return normalize(s1) == normalize(s2)
    count = 0
    for combo in combinations(lst, 2):
        if len(combo[0]) >= 3 and is_anagram(*combo):
            count += 1
        if count >= 8:
            return True
    return False