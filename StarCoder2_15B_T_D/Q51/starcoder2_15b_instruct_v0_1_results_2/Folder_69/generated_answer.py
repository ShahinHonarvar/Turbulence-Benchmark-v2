from itertools import combinations
    from collections import defaultdict

def if_contains_anagrams(list_of_strings):
    """
    This function takes a list of strings and returns True if there are at most 58 pairs of anagrams in the list;
    otherwise, it returns False. Anagrams are considered only for the English letters, and pairs of anagrams must
    have a length of at least three. Anagrams are compared in a case-insensitive manner.
    """
    anagram_pairs = []
    letter_dict = defaultdict(list)
    for string in list_of_strings:
        letters = [letter for letter in string.lower() if letter.isalpha()]
        if len(letters) >= 3:
            letter_dict[tuple(sorted(letters))].append(string)
    for anagrams in letter_dict.values():
        if len(anagrams) > 1:
            anagram_pairs.append(anagrams)
    return len(anagram_pairs) <= 58