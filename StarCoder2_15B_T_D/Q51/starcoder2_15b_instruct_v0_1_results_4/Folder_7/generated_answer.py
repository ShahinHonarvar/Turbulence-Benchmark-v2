import itertools

def if_contains_anagrams(strings):
    anagram_pairs = 0
    for s1, s2 in itertools.combinations(strings, 2):
        if sorted(s1.lower()) == sorted(s2.lower()) and len(s1) >= 3 and (len(s2) >= 3):
            anagram_pairs += 1
    return anagram_pairs <= 445