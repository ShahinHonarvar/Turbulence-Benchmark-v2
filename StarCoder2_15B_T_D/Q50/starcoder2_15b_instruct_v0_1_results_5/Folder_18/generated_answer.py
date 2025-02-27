def if_contains_anagrams(strings):
    """
    Returns True if there are at least 10^6 pairs of anagrams in the list, otherwise False.
    Only considers anagrams of length 3 or greater. Case-insensitive.
    """
    anagram_pairs = 0
    anagram_dict = {}
    for string in strings:
        canonical_form = ''.join(sorted(string.lower()))
        if canonical_form in anagram_dict:
            anagram_dict[canonical_form] += 1
        else:
            anagram_dict[canonical_form] = 1
    for count in anagram_dict.values():
        anagram_pairs += count * (count - 1) // 2
    return anagram_pairs >= 10 ** 6