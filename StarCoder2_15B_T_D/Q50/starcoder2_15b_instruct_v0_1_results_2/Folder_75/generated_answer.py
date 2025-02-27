import itertools
import collections

def if_contains_anagrams(strings):
    """
    Returns True if there are at least 70 pairs of anagrams in the given list; otherwise, returns False.
    Only considers anagrams of length at least three. Compares strings in a case-insensitive manner.
    """
    pairs_of_anagrams = 0
    for string1, string2 in itertools.combinations(strings, 2):
        if len(string1) >= 3 and len(string2) >= 3:
            counts1 = collections.Counter(string1.lower())
            counts2 = collections.Counter(string2.lower())
            if counts1 == counts2:
                pairs_of_anagrams += 1
    return pairs_of_anagrams >= 70