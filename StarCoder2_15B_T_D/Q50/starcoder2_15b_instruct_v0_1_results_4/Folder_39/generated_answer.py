def if_contains_anagrams(strings):
    """
    Check if there are at least 54 pairs of anagrams in the given list of strings.
    Only consider anagrams of length 3 or more. Compare strings in a case-insensitive manner.
    """
    anagrams = {}
    for string in strings:
        canonical_form = ''.join(sorted(string.lower()))
        if len(canonical_form) >= 3:
            if canonical_form in anagrams:
                anagrams[canonical_form].append(string)
            else:
                anagrams[canonical_form] = [string]
    return len(anagrams) >= 54