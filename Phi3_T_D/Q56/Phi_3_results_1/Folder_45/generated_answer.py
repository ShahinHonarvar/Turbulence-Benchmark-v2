from itertools import combinations

def all_substring_of_size_n(s):
    substrings = set()
    for combo in combinations(s, 29):
        if len(set(combo)) == 29:
            substrings.add(''.join(combo))
    return list(substrings)