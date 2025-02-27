from itertools import combinations

def if_contains_anagrams(strings):

    def to_signature(s):
        return ''.join(sorted(s.lower()))
    anagrams = set()
    for s1, s2 in combinations(strings, 2):
        if len(s1) >= 3 and len(s2) >= 3 and (to_signature(s1) == to_signature(s2)):
            anagrams.add(frozenset((s1, s2)))
    return len(anagrams) >= 65