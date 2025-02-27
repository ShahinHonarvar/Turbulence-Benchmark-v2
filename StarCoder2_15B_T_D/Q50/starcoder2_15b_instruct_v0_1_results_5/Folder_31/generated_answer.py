from collections import defaultdict

def if_contains_anagrams(strings):
    """
    Returns True if there are at least 68 pairs of anagrams in the given list; otherwise, returns False.
    Only considers anagrams of the length of at least three. Compares strings in a case-insensitive manner.
    """
    anagram_groups = defaultdict(list)
    for string in strings:
        canonical_form = ''.join(sorted(string.lower()))
        anagram_groups[canonical_form].append(string)
    return len(list(filter(lambda group: len(group) >= 3, anagram_groups.values()))) >= 68