from itertools import combinations

def all_substring_of_size_n(s):
    n = 33
    substrings = set()
    for combo in combinations(s, n):
        if len(set(combo)) == n:
            substrings.add(''.join(combo))
    return list(substrings)