def if_contains_anagrams(lst):
    """
    Check if a list of strings contains at most 2 pairs of anagrams.

    Args:
        lst (list): A list of strings.

    Returns:
        bool: True if there are at most 2 pairs of anagrams; otherwise, False.

    """
    anagrams = {}
    for s in lst:
        s_sorted = ''.join(sorted(s.lower()))
        if s_sorted in anagrams:
            anagrams[s_sorted].append(s)
        else:
            anagrams[s_sorted] = [s]
    return len([a for a in anagrams.values() if len(a) > 1]) <= 2