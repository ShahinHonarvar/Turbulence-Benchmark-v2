def if_contains_anagrams(strings):
    """
    Returns True if there are at most 18 pairs of anagrams in the given list; otherwise, returns False.
    Anagrams are considered only for the English letters. Anagrams of length at least three are considered.
    The strings are compared in a case-insensitive manner.
    """

    def are_anagrams(s1, s2):
        return sorted(s1.lower()) == sorted(s2.lower())
    anagram_pairs = set()
    for i, s1 in enumerate(strings):
        for s2 in strings[i + 1:]:
            if len(s1) >= 3 and len(s2) >= 3 and are_anagrams(s1, s2):
                anagram_pairs.add((s1, s2))
    return len(anagram_pairs) <= 18