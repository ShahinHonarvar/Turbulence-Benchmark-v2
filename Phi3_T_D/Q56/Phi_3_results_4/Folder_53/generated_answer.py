from itertools import combinations

def all_substring_of_size_n(s):
    n = 25
    char_set = set(s)
    if len(char_set) < n:
        return []
    possible_substrings = [''.join(substring) for substring in combinations(char_set, n)]
    return possible_substrings