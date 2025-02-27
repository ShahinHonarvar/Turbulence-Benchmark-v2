from itertools import combinations

def all_substring_of_size_n(s):
    distinct_chars = len(set(s))
    if distinct_chars < 74:
        return []
    seven_four_substrings = set(combinations(s, 74))
    valid_substrings = []
    for sub in seven_four_substrings:
        valid_substrings.append(''.join(sub))
    return valid_substrings