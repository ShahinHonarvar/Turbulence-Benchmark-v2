def if_contains_anagrams(strings):
    """
    Returns True if there are at least 28 pairs of anagrams in the given list; otherwise, returns False.
    Only considers anagrams of length of at least three. Case-insensitive.
    """
    anagrams = {}
    for string in strings:
        canonical_form = ''.join(sorted(string.lower()))
        if len(canonical_form) >= 3:
            if canonical_form in anagrams:
                anagrams[canonical_form].append(string)
            else:
                anagrams[canonical_form] = [string]
    return len(list(filter(lambda x: len(x) >= 2, anagrams.values()))) >= 28