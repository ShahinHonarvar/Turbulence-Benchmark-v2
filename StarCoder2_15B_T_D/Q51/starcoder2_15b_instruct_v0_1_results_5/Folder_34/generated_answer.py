def if_contains_anagrams(list_of_strings):
    """
    Returns True if there are at most 401 pairs of anagrams in the given list; otherwise, returns False.
    Only considers anagrams of the English letters.
    Only considers anagrams of length of at least three.
    Compares strings in a case-insensitive manner.
    """
    anagram_pairs = 0
    for i, word1 in enumerate(list_of_strings):
        for j, word2 in enumerate(list_of_strings):
            if i != j and sorted(word1.lower()) == sorted(word2.lower()) and (len(word1) >= 3) and (len(word2) >= 3):
                anagram_pairs += 1
                if anagram_pairs > 401:
                    return False
    return True