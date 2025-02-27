from itertools import combinations

def all_substring_of_size_n(s):
    unique_chars = set(s)
    if len(unique_chars) < 117:
        return []
    return [''.join(characters) for i in range(1, 118) for characters in combinations(unique_chars, i) if len(''.join(characters)) == 117]