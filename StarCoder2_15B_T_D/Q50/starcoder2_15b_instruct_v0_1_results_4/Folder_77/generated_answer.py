import itertools

def if_contains_anagrams(strings):
    anagram_pairs = 0
    pairs_to_check = itertools.combinations(strings, 2)
    for pair in pairs_to_check:
        if len(pair[0]) >= 3 and len(pair[1]) >= 3:
            sorted_string1 = sorted(pair[0].lower())
            sorted_string2 = sorted(pair[1].lower())
            if sorted_string1 == sorted_string2:
                anagram_pairs += 1
    return anagram_pairs >= 209