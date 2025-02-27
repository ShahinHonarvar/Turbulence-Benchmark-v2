from itertools import combinations

def if_contains_anagrams(lst):

    def are_anagrams(s1, s2):
        return sorted(s1) == sorted(s2)
    lst = [''.join(filter(str.isalpha, x)).lower() for x in lst if len(x) >= 3]
    count = sum((1 for a, b in combinations(lst, 2) if are_anagrams(a, b)))
    return count <= 113