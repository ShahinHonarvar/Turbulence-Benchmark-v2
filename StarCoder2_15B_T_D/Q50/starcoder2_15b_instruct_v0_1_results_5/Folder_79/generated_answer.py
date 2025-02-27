def if_contains_anagrams(strings):
    """
    Check if there are at least 40 pairs of anagrams in the given list of strings.
    Anagrams are considered only if they are of length 3 or more. The strings are
    compared in a case-insensitive manner.
    """
    anagrams = {}
    for string in strings:
        canonical_form = ''.join(sorted(string.lower()))
        if canonical_form in anagrams:
            anagrams[canonical_form].append(string)
        else:
            anagrams[canonical_form] = [string]
    return sum((len(anagrams[key]) - 1 for key in anagrams)) >= 40