def if_contains_anagrams(strings):
    """
    Returns True if there are at most 75 pairs of anagrams in the given list;
    otherwise, returns False.
    """
    anagrams = {}
    for string in strings:
        normalized = ''.join((c for c in string.lower() if c.isalpha()))
        if len(normalized) >= 3:
            anagram_key = ''.join(sorted(normalized))
            anagrams[anagram_key] = anagrams.get(anagram_key, []) + [string]
    return len(list(filter(lambda x: len(x) > 1, anagrams.values()))) <= 75