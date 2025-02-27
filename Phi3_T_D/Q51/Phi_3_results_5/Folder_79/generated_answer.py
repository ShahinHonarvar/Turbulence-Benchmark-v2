from itertools import combinations

def if_contains_anagrams(strings):

    def normalize(s):
        return ''.join(sorted(s.lower()))
    anagram_count = sum((normalize(s1) == normalize(s2) for s1, s2 in combinations(strings, 2)))
    return anagram_count <= 173