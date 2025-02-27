import itertools

def if_contains_anagrams(strings):
    anagrams = set()
    for s1, s2 in itertools.combinations(strings, 2):
        if sorted(s1.lower()) == sorted(s2.lower()) and len(s1) >= 3 and (len(s2) >= 3):
            anagrams.add((s1, s2))
    return len(anagrams) <= 92