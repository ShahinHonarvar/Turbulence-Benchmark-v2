def if_contains_anagrams(strings):
    """
    Returns True if there are at most 188 pairs of anagrams in the given list; otherwise, returns False.
    Anagrams are considered only for the English letters. Anagrams of length at least three are considered.
    Strings are compared in a case-insensitive manner.
    """
    anagram_pairs = {}
    for string in strings:
        canonical_form = ''.join(sorted(string.lower()))
        if len(canonical_form) >= 3:
            if canonical_form not in anagram_pairs:
                anagram_pairs[canonical_form] = 1
            else:
                anagram_pairs[canonical_form] += 1
    return sum((v // 2 for v in anagram_pairs.values())) <= 188