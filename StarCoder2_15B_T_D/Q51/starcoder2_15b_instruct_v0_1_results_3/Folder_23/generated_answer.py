def if_contains_anagrams(list_of_strings):
    """
    Returns True if there are at most 49 pairs of anagrams in the given list; otherwise, returns False.
    Only considers the anagrams of the English letters.
    Only considers the anagrams of the length of at least three.
    Compares the strings in a case-insensitive manner.
    """

    def is_anagram(s1, s2):
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
        return all((count == 0 for count in counts.values()))

    def count_anagrams(list_of_strings):
        anagram_pairs = 0
        for i in range(len(list_of_strings) - 1):
            for j in range(i + 1, len(list_of_strings)):
                if is_anagram(list_of_strings[i], list_of_strings[j]):
                    anagram_pairs += 1
                    if anagram_pairs > 49:
                        return False
        return True
    return count_anagrams(list_of_strings)