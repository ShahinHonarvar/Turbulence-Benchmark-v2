def if_contains_anagrams(strings):
    """
    Return True if there are at most 18 pairs of anagrams in the given list; otherwise, return False.
    Only consider the anagrams of the English letters. Only consider the anagrams of the length of at least three.
    Compare the strings in a case-insensitive manner.
    """
    anagrams = {}
    for s in strings:
        canonical_form = ''.join(sorted(s.lower()))
        if canonical_form in anagrams:
            anagrams[canonical_form].append(s)
        else:
            anagrams[canonical_form] = [s]
    num_anagrams = 0
    for anagram_group in anagrams.values():
        if len(anagram_group) >= 3:
            num_anagrams += len(anagram_group) // 2
    return num_anagrams <= 18