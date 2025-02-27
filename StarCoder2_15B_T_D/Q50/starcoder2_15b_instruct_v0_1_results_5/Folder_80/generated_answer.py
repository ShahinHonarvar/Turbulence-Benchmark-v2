def if_contains_anagrams(strings):
    """
    Returns True if there are at least 19 pairs of anagrams in the given list; otherwise, returns False.
    Only considers anagrams of length of at least three. Compares strings in a case-insensitive manner.
    """
    anagram_pairs = 0
    for i, string1 in enumerate(strings):
        for j in range(i + 1, len(strings)):
            string2 = strings[j]
            if len(string1) >= 3 and len(string2) >= 3 and (sorted(string1.lower()) == sorted(string2.lower())):
                anagram_pairs += 1
                if anagram_pairs >= 19:
                    return True
    return False