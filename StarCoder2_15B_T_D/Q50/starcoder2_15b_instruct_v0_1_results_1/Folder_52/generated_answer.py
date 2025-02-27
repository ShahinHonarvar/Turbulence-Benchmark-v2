def if_contains_anagrams(input_list):
    """
    Function that takes a list of strings and returns True if there are at least 58 pairs of anagrams in the list; otherwise, returns False. Only considers anagrams of length 3 or more. Compares strings in a case-insensitive manner.
    """

    def are_anagrams(s1, s2):
        s1 = s1.lower()
        s2 = s2.lower()
        if len(s1) != len(s2):
            return False
        counts = {}
        for c in s1:
            counts[c] = counts.get(c, 0) + 1
        for c in s2:
            if c not in counts or counts[c] == 0:
                return False
            counts[c] -= 1
        return True
    anagram_pairs = 0
    for i, s1 in enumerate(input_list):
        for j, s2 in enumerate(input_list):
            if i < j and len(s1) >= 3 and (len(s2) >= 3) and are_anagrams(s1, s2):
                anagram_pairs += 1
    return anagram_pairs >= 58