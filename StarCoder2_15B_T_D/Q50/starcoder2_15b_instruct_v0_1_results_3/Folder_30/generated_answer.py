import itertools

def if_contains_anagrams(strings):
    anagram_pairs = 0
    for string1, string2 in itertools.combinations(strings, 2):
        if len(string1) >= 3 and len(string2) >= 3 and (sorted(string1.lower()) == sorted(string2.lower())):
            anagram_pairs += 1
    return anagram_pairs >= 78