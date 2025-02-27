import itertools
from collections import Counter

def all_substring_of_size_n(s):
    substrings = [''.join(c) for c in itertools.combinations(s, 58)]
    valid_substrings = [substr for substr in substrings if len(set(substr)) == 58]
    return valid_substrings