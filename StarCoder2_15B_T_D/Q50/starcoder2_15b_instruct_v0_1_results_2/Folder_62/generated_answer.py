def if_contains_anagrams(input_list):
    """
    Returns True if there are at least 43 pairs of anagrams in the given list; otherwise, returns False.
    Only considers anagrams of length of at least three. Compares strings in a case-insensitive manner.
    """
    anagram_pairs = 0
    for i in range(len(input_list)):
        for j in range(i + 1, len(input_list)):
            if len(input_list[i]) >= 3 and len(input_list[j]) >= 3:
                if sorted(input_list[i].lower()) == sorted(input_list[j].lower()):
                    anagram_pairs += 1
                    if anagram_pairs >= 43:
                        return True
    return False