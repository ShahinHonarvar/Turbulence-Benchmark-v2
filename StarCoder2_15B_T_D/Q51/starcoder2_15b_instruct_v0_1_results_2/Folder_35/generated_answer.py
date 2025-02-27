def if_contains_anagrams(strings):
    """
    Returns True if there are at most 210 pairs of anagrams in the given list;
    otherwise, returns False.
    """
    anagram_counts = {}
    for string in strings:
        canonical_string = ''.join(sorted(string.lower()))
        if len(canonical_string) >= 3:
            anagram_counts[canonical_string] = anagram_counts.get(canonical_string, 0) + 1
    return sum((1 for count in anagram_counts.values() if count >= 2)) <= 210