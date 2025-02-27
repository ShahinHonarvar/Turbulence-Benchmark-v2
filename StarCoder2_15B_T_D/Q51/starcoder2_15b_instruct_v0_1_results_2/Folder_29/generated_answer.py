import itertools

def if_contains_anagrams(list_of_strings):
    """
    This function takes one argument, a list of strings.
    It returns true if there are at most 318 pairs of anagrams in the given list; otherwise, it returns false.
    It only considers the anagrams of the English letters.
    It only considers the anagrams of the length of at least three.
    It compares the strings in a case-insensitive manner.
    """
    anagrams = {}
    for i, j in itertools.combinations(range(len(list_of_strings)), 2):
        s1, s2 = (list_of_strings[i].lower(), list_of_strings[j].lower())
        if len(s1) >= 3 and len(s2) >= 3 and (sorted(s1) == sorted(s2)):
            anagrams[s1, s2] = (i, j)
    return len(anagrams) <= 318