def if_contains_anagrams(list_of_strings):
    """
    Check if there are at least 72 pairs of anagrams in the given list of strings.
    Only consider anagrams of length at least three. Compare strings in a case-insensitive manner.
    """
    anagrams = {}
    for string in list_of_strings:
        canonical_form = ''.join(sorted(string.lower()))
        if len(canonical_form) >= 3:
            if canonical_form in anagrams:
                anagrams[canonical_form].append(string)
            else:
                anagrams[canonical_form] = [string]
    return sum((len(v) - 1 for v in anagrams.values())) >= 72