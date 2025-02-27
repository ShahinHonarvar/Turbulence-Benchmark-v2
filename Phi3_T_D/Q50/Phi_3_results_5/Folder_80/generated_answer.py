from itertools import combinations

def if_contains_anagrams(lst):

    def normalize(s):
        return ''.join(sorted(s.lower()))
    count = sum((1 for x, y in combinations(lst, 2) if len(x) >= 3 and len(y) >= 3 and (normalize(x) == normalize(y))))
    return count >= 19