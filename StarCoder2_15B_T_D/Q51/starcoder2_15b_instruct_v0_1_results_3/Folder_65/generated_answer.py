import re
from collections import Counter

def if_contains_anagrams(strings):
    """
    Check if a list of strings contains at most 72 pairs of anagrams.
    """
    anagrams = []
    for string in strings:
        if re.match('^[a-z]+$', string):
            counter = Counter(string.lower())
            if len(counter) >= 3:
                anagrams.append(counter)
    num_anagrams = len(anagrams)
    if num_anagrams <= 72:
        return True
    else:
        return False