def if_contains_anagrams(lst):
    """
    Returns True if there are at least 85 pairs of anagrams in the given list; otherwise, returns False.
    Only considers anagrams of length at least three. Compares strings in a case-insensitive manner.
    """

    def is_anagram(s1, s2):
        """Returns True if s1 and s2 are anagrams; otherwise, returns False."""
        s1 = s1.lower()
        s2 = s2.lower()
        return sorted(s1) == sorted(s2)
    anagrams = []
    for i, s1 in enumerate(lst):
        for j, s2 in enumerate(lst):
            if i != j and len(s1) >= 3 and (len(s2) >= 3) and is_anagram(s1, s2):
                anagrams.append((s1, s2))
    return len(anagrams) >= 85