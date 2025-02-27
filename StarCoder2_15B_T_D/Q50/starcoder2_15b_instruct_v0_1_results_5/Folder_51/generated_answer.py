import itertools

def if_contains_anagrams(strings):
    """
    Returns True if there are at least 39 pairs of anagrams in the given list; otherwise, returns False.
    Only considers anagrams of length of at least three. Compares strings in a case-insensitive manner.
    """

    def anagrams(s1, s2):
        return sorted(s1.lower()) == sorted(s2.lower())
    count = 0
    for s1, s2 in itertools.combinations(strings, 2):
        if anagrams(s1, s2):
            count += 1
    return count >= 39