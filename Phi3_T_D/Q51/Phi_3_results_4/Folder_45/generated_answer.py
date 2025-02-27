from itertools import combinations

def if_contains_anagrams(strings):

    def normalize(s):
        return ''.join(sorted(s.lower()))
    anagram_count = sum((1 for s1, s2 in combinations(strings, 2) if len(s1) >= 3 and len(s2) >= 3 and (normalize(s1) == normalize(s2))))
    return anagram_count <= 464