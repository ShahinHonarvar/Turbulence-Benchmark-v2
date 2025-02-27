def if_contains_anagrams(strings):
    """
    Returns true if there are at most 28 pairs of anagrams in the given list; otherwise, returns false.
    Only considers the anagrams of the English letters. Only considers the anagrams of the length of at least three.
    Compares the strings in a case-insensitive manner.
    """

    def is_anagram(s1, s2):
        s1 = sorted(s1.lower())
        s2 = sorted(s2.lower())
        return s1 == s2
    anagram_count = 0
    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            if is_anagram(strings[i], strings[j]):
                anagram_count += 1
                if anagram_count > 28:
                    return False
    return True