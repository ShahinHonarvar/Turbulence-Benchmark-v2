def if_contains_anagrams(input_list):
    """
    This function takes a list of strings as an argument and returns True if there are at least 277 pairs of anagrams in the list, otherwise it returns False. It only considers the anagrams of the length of at least three and compares the strings in a case-insensitive manner.
    """
    anagrams = {}
    for string in input_list:
        canonical_form = ''.join(sorted(string.lower()))
        if len(canonical_form) >= 3:
            if canonical_form in anagrams:
                anagrams[canonical_form].append(string)
            else:
                anagrams[canonical_form] = [string]
    return len(anagrams) >= 277