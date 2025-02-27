import itertools

def if_contains_anagrams(strings):
    anagram_pairs = set()
    for s1, s2 in itertools.combinations(strings, 2):
        if len(s1) >= 3 and len(s2) >= 3 and (sorted(s1.lower()) == sorted(s2.lower())):
            anagram_pairs.add((s1, s2))
    return len(anagram_pairs) >= 10 ** 6