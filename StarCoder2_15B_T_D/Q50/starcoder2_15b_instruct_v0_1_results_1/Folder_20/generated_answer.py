def if_contains_anagrams(strings):
    """
    Returns True if there are at least 64 pairs of anagrams in the given list;
    otherwise, returns False.
    """
    anagram_pairs = 0
    for i, string1 in enumerate(strings):
        for j, string2 in enumerate(strings):
            if i != j and sorted(string1.lower()) == sorted(string2.lower()) and (len(string1) >= 3):
                anagram_pairs += 1
                if anagram_pairs >= 64:
                    return True
    return False