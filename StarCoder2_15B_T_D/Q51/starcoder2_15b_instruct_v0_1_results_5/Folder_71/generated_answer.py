def if_contains_anagrams(list_of_strings):
    """
    Write a function called 'if_contains_anagrams' that takes one argument, a list of strings.
    The function should return true if there are at most 9 pairs of anagrams in the given list;
    otherwise, it should return false. The function should only consider the anagrams of the
    English letters. The function should only consider the anagrams of the length of at least three.
    The function should compare the strings in a case-insensitive manner.
    """
    anagrams = {}
    for string in list_of_strings:
        key = ''.join(sorted(string.lower()))
        if len(key) >= 3:
            if key in anagrams:
                anagrams[key] += 1
            else:
                anagrams[key] = 1
    return max(anagrams.values()) <= 9