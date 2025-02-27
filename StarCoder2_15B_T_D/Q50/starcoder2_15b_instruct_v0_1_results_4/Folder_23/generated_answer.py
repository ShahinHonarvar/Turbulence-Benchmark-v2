def if_contains_anagrams(strings):
    """
    Returns True if there are at least 67 pairs of anagrams in the given list;
    otherwise, returns False. Anagrams are considered only if they are of length
    at least three and are compared in a case-insensitive manner.
    """
    anagram_counts = {}
    for string in strings:
        canonical_form = ''.join(sorted(string.lower()))
        if len(canonical_form) >= 3:
            if canonical_form in anagram_counts:
                anagram_counts[canonical_form] += 1
            else:
                anagram_counts[canonical_form] = 1
    return sum((1 for count in anagram_counts.values() if count >= 2)) >= 67