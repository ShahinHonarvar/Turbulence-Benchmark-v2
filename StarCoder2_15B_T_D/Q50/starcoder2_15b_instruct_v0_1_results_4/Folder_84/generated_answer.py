def if_contains_anagrams(list_of_strings):
    """
    Returns True if there are at least 108 pairs of anagrams in the given list; otherwise, returns False.
    Only considers anagrams of length at least three. Compares strings in a case-insensitive manner.
    """
    anagrams = {}
    for string in list_of_strings:
        key = ''.join(sorted(string.lower()))
        if key in anagrams:
            anagrams[key].append(string)
        else:
            anagrams[key] = [string]
    return sum((len(v) - 1 for v in anagrams.values())) >= 108