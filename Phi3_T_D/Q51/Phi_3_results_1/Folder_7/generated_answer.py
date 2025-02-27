from itertools import combinations

def if_contains_anagrams(strings):

    def normalize(s):
        return ''.join(sorted(s.lower()))
    anagram_pairs = set()
    for s1, s2 in combinations(strings, 2):
        if len(s1) >= 3 and len(s2) >= 3:
            if normalize(s1) == normalize(s2):
                anagram_pairs.add(frozenset([s1, s2]))
    return len(anagram_pairs) <= 445