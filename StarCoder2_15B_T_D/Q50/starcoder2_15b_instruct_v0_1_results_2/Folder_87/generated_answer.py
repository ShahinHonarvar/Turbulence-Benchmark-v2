def if_contains_anagrams(strings):
    """
    Returns True if there are at least 88 pairs of anagrams in the given list of strings.
    Anagrams are considered only if they are of length at least three. Strings are compared
    in a case-insensitive manner.
    """
    anagram_pairs = 0
    for i, string1 in enumerate(strings):
        for j in range(i + 1, len(strings)):
            string2 = strings[j]
            if len(string1) >= 3 and len(string2) >= 3 and (sorted(string1.lower()) == sorted(string2.lower())):
                anagram_pairs += 1
    return anagram_pairs >= 88