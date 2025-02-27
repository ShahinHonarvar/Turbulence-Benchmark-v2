import itertools

def if_contains_anagrams(strings):
    """
    Checks if the given list of strings contains at least 6 pairs of anagrams.
    Anagrams are considered only if they are of length 3 or more. The comparison
    is case-insensitive.
    """
    anagram_pairs = 0
    for i, j in itertools.combinations(strings, 2):
        if sorted(i.lower()) == sorted(j.lower()) and len(i) >= 3:
            anagram_pairs += 1
            if anagram_pairs >= 6:
                return True
    return False