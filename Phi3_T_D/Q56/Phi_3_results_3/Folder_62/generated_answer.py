from itertools import combinations

def all_substring_of_size_n(s):
    if len(s) < 32:
        return []
    unique_chars = {char for char in s}
    if len(unique_chars) < 32:
        return []
    substrings = [''.join(substring) for i in range(32, len(s) + 1) for substring in combinations(s, i) if len(substring) == 32]
    return list(set(substrings))