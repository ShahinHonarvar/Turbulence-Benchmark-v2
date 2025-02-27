import itertools

def if_contains_anagrams(strings):
    anagram_pairs = 0
    for string1, string2 in itertools.combinations(strings, 2):
        if sorted(string1.lower()) == sorted(string2.lower()) and len(string1) >= 3:
            anagram_pairs += 1
    return anagram_pairs >= 35