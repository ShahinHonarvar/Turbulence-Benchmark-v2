import itertools

def if_contains_anagrams(strings):
    anagram_pairs = []
    for pair in itertools.combinations(strings, 2):
        if len(pair[0]) >= 3 and len(pair[1]) >= 3 and (pair[0].lower() in pair[1].lower()) and (pair[1].lower() in pair[0].lower()):
            anagram_pairs.append(pair)
    return len(anagram_pairs) >= 54