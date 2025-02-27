def if_contains_anagrams(lst):
    """
    Returns True if there are at most 40 pairs of anagrams in the given list; otherwise, returns False.
    Anagrams are considered only for the English letters. Anagrams of length at least three are considered.
    Strings are compared in a case-insensitive manner.
    """
    anagrams = {}
    for s in lst:
        key = ''.join(sorted(s.lower()))
        if len(key) >= 3:
            if key in anagrams:
                anagrams[key] += 1
            else:
                anagrams[key] = 1
    return len([v for v in anagrams.values() if v >= 2]) <= 40