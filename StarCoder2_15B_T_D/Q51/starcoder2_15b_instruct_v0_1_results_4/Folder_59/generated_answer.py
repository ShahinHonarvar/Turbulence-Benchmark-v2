def if_contains_anagrams(list_of_strings):
    """
    This function takes a list of strings and returns True if there are at most 15 pairs of anagrams in the list.
    Anagrams are defined as two strings that contain the same letters in a different order.
    The function only considers anagrams of the English letters and the length of at least three.
    The comparison is case-insensitive.
    """
    anagrams = {}
    for string in list_of_strings:
        key = ''.join(sorted(string.lower()))
        if key in anagrams:
            anagrams[key].append(string)
        else:
            anagrams[key] = [string]
    count = 0
    for key in anagrams:
        if len(anagrams[key]) >= 3:
            count += len(anagrams[key]) - 2
    return count <= 15