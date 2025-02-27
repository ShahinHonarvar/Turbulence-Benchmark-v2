def if_contains_anagrams(input_list):
    """
    Returns True if there are at most 47 pairs of anagrams in the given list; otherwise, returns False.
    Anagrams are defined as strings that contain the same letters in a different order.
    Only anagrams of the English letters are considered.
    Only anagrams of length of at least three are considered.
    Strings are compared in a case-insensitive manner.
    """

    def is_anagram(s1, s2):
        s1 = ''.join((ch for ch in s1 if ch.isalpha())).lower()
        s2 = ''.join((ch for ch in s2 if ch.isalpha())).lower()
        return sorted(s1) == sorted(s2) and len(s1) >= 3
    anagram_pairs = []
    for i, s1 in enumerate(input_list):
        for j, s2 in enumerate(input_list):
            if i < j and is_anagram(s1, s2):
                anagram_pairs.append((s1, s2))
    return len(anagram_pairs) <= 47