import itertools

def if_contains_anagrams(strings):
    strings = [s.lower() for s in strings]
    strings = [s for s in strings if len(s) >= 3]
    pairs = itertools.combinations(strings, 2)
    anagram_pairs = [(s1, s2) for s1, s2 in pairs if sorted(s1) == sorted(s2)]
    return len(anagram_pairs) >= 94