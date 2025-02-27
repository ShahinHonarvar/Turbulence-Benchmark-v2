def if_contains_anagrams(strings):
    """
    This function takes a list of strings as an argument and returns True if there
    are at least 49 pairs of anagrams in the list; otherwise, it returns False.
    The function considers anagrams of length at least three and compares strings
    in a case-insensitive manner.
    """

    def are_anagrams(s1, s2):
        """
        This helper function checks if two strings are anagrams of each other.
        The function considers anagrams of length at least three and compares
        strings in a case-insensitive manner.
        """
        if len(s1) >= 3 and len(s2) >= 3:
            s1_sorted = sorted(s1.lower())
            s2_sorted = sorted(s2.lower())
            return s1_sorted == s2_sorted
        else:
            return False
    anagram_pairs = 0
    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            if are_anagrams(strings[i], strings[j]):
                anagram_pairs += 1
                if anagram_pairs >= 49:
                    return True
    return False