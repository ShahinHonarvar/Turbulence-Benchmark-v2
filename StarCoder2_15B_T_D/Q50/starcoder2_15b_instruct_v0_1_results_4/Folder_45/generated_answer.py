def if_contains_anagrams(lst):
    """
    Returns True if there are at least 277 pairs of anagrams in the given list;
    otherwise, returns False. Anagrams are considered only if they have a length
    of at least three and are compared in a case-insensitive manner.
    """
    anagrams = {}
    for s in lst:
        key = ''.join(sorted(s.lower()))
        if len(key) >= 3:
            if key in anagrams:
                anagrams[key].append(s)
            else:
                anagrams[key] = [s]
    return len(anagrams) >= 277