def if_contains_anagrams(strings):
    """
    Function to check if a list of strings contains at least 81 pairs of anagrams.
    The function only considers anagrams of length at least three and compares
    strings in a case-insensitive manner.
    """
    anagram_pairs = 0
    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            if len(strings[i]) >= 3 and len(strings[j]) >= 3:
                if sorted(strings[i].lower()) == sorted(strings[j].lower()):
                    anagram_pairs += 1
                    if anagram_pairs >= 81:
                        return True
    return False