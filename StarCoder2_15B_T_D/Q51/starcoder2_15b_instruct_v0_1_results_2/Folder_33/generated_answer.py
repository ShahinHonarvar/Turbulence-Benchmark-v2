def if_contains_anagrams(input_list):
    """
    Check if a list of strings contains at most 85 pairs of anagrams.
    Anagrams are considered only for the English letters, and only
    pairs of anagrams of length at least three are considered.
    """

    def is_anagram(s1, s2):
        s1 = ''.join((c for c in s1 if c.isalpha())).lower()
        s2 = ''.join((c for c in s2 if c.isalpha())).lower()
        return sorted(s1) == sorted(s2) and len(s1) >= 3
    anagrams = []
    for i, s1 in enumerate(input_list):
        for s2 in input_list[i + 1:]:
            if is_anagram(s1, s2):
                anagrams.append((s1, s2))
    return len(anagrams) <= 85