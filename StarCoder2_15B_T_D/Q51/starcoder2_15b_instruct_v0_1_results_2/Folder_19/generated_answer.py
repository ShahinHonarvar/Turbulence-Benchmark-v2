import collections

def if_contains_anagrams(lst):
    """
    Returns True if there are at most 69 pairs of anagrams in the given list; otherwise, returns False.
    Only considers the anagrams of the English letters.
    Only considers the anagrams of the length of at least three.
    Compares the strings in a case-insensitive manner.
    """
    anagram_pairs = 0
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if len(lst[i]) >= 3 and len(lst[j]) >= 3 and (sorted(lst[i].lower()) == sorted(lst[j].lower())):
                anagram_pairs += 1
                if anagram_pairs > 69:
                    return False
    return True