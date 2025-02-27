from itertools import combinations

def if_contains_anagrams(strings):

    def normalize(s):
        return ''.join(sorted(s.lower()))

    def count_anagrams(s_list):
        return sum((1 for s1, s2 in combinations(s_list, 2) if normalize(s1) == normalize(s2)))
    return count_anagrams(strings) <= 181