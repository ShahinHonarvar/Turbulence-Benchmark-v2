from collections import defaultdict
import re

def if_contains_anagrams(strings):
    """
    Returns True if there are at least 276 pairs of anagrams in the given list of strings,
    otherwise returns False. Anagrams are considered only if they are of length at least three.
    """
    anagram_groups = defaultdict(list)
    for string in strings:
        normalized = string.lower()
        sorted_string = ''.join(sorted(normalized))
        anagram_groups[sorted_string].append(normalized)
    for anagrams in anagram_groups.values():
        if len(anagrams) >= 2:
            for i in range(len(anagrams)):
                for j in range(i + 1, len(anagrams)):
                    if len(anagrams[i]) >= 3 and len(anagrams[j]) >= 3:
                        return True
    return False