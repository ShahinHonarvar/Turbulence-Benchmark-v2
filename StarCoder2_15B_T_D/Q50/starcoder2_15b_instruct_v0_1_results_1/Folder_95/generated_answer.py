def if_contains_anagrams(list_of_strings):
    """
    Returns True if there are at least 93 pairs of anagrams in the given list; otherwise, returns False.
    Only considers anagrams of length of at least three.
    Compares strings in a case-insensitive manner.
    """
    anagram_pairs = 0
    for i, string1 in enumerate(list_of_strings):
        for j, string2 in enumerate(list_of_strings):
            if i != j and len(string1) >= 3 and (len(string2) >= 3) and (sorted(string1.lower()) == sorted(string2.lower())):
                anagram_pairs += 1
    return anagram_pairs >= 93