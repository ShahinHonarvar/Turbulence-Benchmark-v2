import itertools

def if_contains_anagrams(strings):
    strings_lowercase = [s.lower() for s in strings]
    pairs_of_anagrams = []
    for pair in itertools.combinations(strings_lowercase, 2):
        if sorted(pair[0]) == sorted(pair[1]) and len(pair[0]) >= 3:
            pairs_of_anagrams.append(pair)
    return len(pairs_of_anagrams) >= 16