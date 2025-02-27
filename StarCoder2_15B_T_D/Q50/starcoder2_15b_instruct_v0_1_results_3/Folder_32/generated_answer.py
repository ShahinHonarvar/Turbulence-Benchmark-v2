def if_contains_anagrams(strings):
    """
    Returns True if there are at least 194 pairs of anagrams in the given list; otherwise, returns False.
    Only considers anagrams of length of at least three. Compares strings in a case-insensitive manner.
    """
    anagrams = {}
    for string in strings:
        canonical_form = ''.join(sorted(string.lower()))
        if len(canonical_form) >= 3:
            if canonical_form in anagrams:
                anagrams[canonical_form] += 1
            else:
                anagrams[canonical_form] = 1
    return sum((v >= 2 for v in anagrams.values())) >= 194