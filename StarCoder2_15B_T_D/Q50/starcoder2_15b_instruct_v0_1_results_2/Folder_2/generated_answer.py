def if_contains_anagrams(list_of_strings):
    """
    Returns True if there are at least 246 pairs of anagrams in the given list; otherwise, returns False.
    Anagrams are considered only if they are of the length of at least three.
    The comparison is case-insensitive.
    """
    anagram_pairs = 0
    for i, string1 in enumerate(list_of_strings):
        for j, string2 in enumerate(list_of_strings):
            if i != j and len(string1) >= 3 and (len(string2) >= 3) and (sorted(string1.lower()) == sorted(string2.lower())):
                anagram_pairs += 1
    return anagram_pairs >= 246