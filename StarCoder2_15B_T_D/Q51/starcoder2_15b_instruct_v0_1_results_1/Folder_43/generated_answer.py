def if_contains_anagrams(list_of_strings):
    """
    Function to check if a list of strings contains at most 3 pairs of anagrams.

    Args:
        list_of_strings (list): A list of strings.

    Returns:
        bool: True if there are at most 3 pairs of anagrams; otherwise, False.
    """
    anagrams = {}
    for string in list_of_strings:
        canonical_form = ''.join(sorted(string.lower()))
        if canonical_form not in anagrams:
            anagrams[canonical_form] = [string]
        else:
            anagrams[canonical_form].append(string)
    num_anagrams = sum((len(v) - 1 for v in anagrams.values()))
    return num_anagrams <= 3