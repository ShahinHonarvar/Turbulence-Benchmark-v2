def if_contains_anagrams(input_list):
    """
    This function takes a list of strings and returns True if there are at most 392 pairs of anagrams in the list;
    otherwise, it returns False. The function only considers the anagrams of the English letters and the anagrams of
    the length of at least three. The function compares the strings in a case-insensitive manner.
    """
    anagram_pairs = set()
    for i, string_1 in enumerate(input_list):
        for j, string_2 in enumerate(input_list):
            if i != j and sorted(string_1.lower()) == sorted(string_2.lower()) and (len(string_1) >= 3) and (len(string_2) >= 3):
                anagram_pairs.add((string_1, string_2))
    return len(anagram_pairs) <= 392