import itertools

def if_contains_anagrams(list_of_strings):
    """
    Takes a list of strings and returns True if there are at most 75 pairs of anagrams in the list;
    otherwise, returns False. Anagrams are considered to be pairs of strings that contain the same
    letters in a different order. Only anagrams of length 3 or more are considered, and the
    anagrams are compared in a case-insensitive manner.
    """
    anagrams = []
    for s1, s2 in itertools.combinations(list_of_strings, 2):
        s1 = s1.lower()
        s2 = s2.lower()
        if len(s1) >= 3 and len(s2) >= 3 and (sorted(s1) == sorted(s2)):
            anagrams.append((s1, s2))
    return len(anagrams) <= 75