import re
from typing import List

def if_contains_anagrams(strings: List[str]) -> bool:
    """
    Returns True if there are at least 20 pairs of anagrams in the given list;
    otherwise, returns False. Anagrams are considered only if they are of length
    at least three. Case-insensitive comparison is used.
    """
    anagrams = {}
    for string in strings:
        canonical = ''.join(sorted(string.lower()))
        if canonical in anagrams:
            anagrams[canonical].append(string)
        else:
            anagrams[canonical] = [string]
    return any((len(v) >= 20 for v in anagrams.values()))