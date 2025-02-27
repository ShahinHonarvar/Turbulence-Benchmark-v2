def if_contains_anagrams(strings):
    """
    Returns `True` if there are at most 42 pairs of anagrams in `strings`;
    otherwise, returns `False`.
    """
    anagram_groups = {}
    for string in strings:
        canonical_form = ''.join(sorted(string.lower()))
        if canonical_form not in anagram_groups:
            anagram_groups[canonical_form] = [string]
        else:
            anagram_groups[canonical_form].append(string)
    return sum((len(group) - 1 for group in anagram_groups.values())) <= 42