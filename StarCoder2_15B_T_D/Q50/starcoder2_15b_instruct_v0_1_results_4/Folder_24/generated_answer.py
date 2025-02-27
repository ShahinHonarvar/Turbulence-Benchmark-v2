def if_contains_anagrams(input_list):
    """
    Checks if there are at least 65 pairs of anagrams in the given list.
    Anagrams are considered only if they are of length at least three.
    The strings are compared in a case-insensitive manner.
    """
    anagrams = {}
    for string in input_list:
        canonical_form = ''.join(sorted(string.lower()))
        if len(canonical_form) >= 3:
            if canonical_form in anagrams:
                anagrams[canonical_form] += 1
            else:
                anagrams[canonical_form] = 1
    return sum((v >= 2 for v in anagrams.values())) >= 65