def if_contains_anagrams(string_list):
    """
    Return True if there are at most 86 pairs of anagrams in the given list; otherwise, return False.
    Anagrams are considered only of the English letters. Anagrams of length at least three are considered.
    Strings are compared in a case-insensitive manner.
    """

    def are_anagrams(s1, s2):
        return sorted(s1.lower()) == sorted(s2.lower())
    anagram_count = 0
    for i in range(len(string_list)):
        for j in range(i + 1, len(string_list)):
            if are_anagrams(string_list[i], string_list[j]):
                anagram_count += 1
                if anagram_count > 86:
                    return False
    return True