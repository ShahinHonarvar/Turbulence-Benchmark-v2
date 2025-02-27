from collections import Counter
from itertools import combinations

def if_contains_anagrams(strings):
    """
    Returns True if there are at most 86 pairs of anagrams in the given list;
    otherwise, returns False.
    """
    anagrams = {}
    for s in strings:
        s_lowercase = s.lower()
        s_filtered = ''.join((c for c in s_lowercase if c.isalpha()))
        if len(s_filtered) >= 3:
            s_sorted = ''.join(sorted(s_filtered))
            if s_sorted not in anagrams:
                anagrams[s_sorted] = [s]
            else:
                anagrams[s_sorted].append(s)
    num_pairs = sum((len(v) * (len(v) - 1) // 2 for v in anagrams.values()))
    return num_pairs <= 86