import itertools

def if_contains_anagrams(input_list):
    anagram_pairs = []
    for pair in itertools.combinations(input_list, 2):
        if sorted(pair[0].lower()) == sorted(pair[1].lower()) and len(pair[0]) >= 3:
            anagram_pairs.append(pair)
    return len(anagram_pairs) >= 189