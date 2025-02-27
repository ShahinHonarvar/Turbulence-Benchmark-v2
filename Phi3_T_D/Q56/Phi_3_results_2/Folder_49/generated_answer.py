from itertools import combinations

def all_substring_of_size_n(s):
    unique_substrings = {''.join(sorted(sub)) for i in range(73) for sub in combinations(s, i) if len(set(sub)) == 73}
    return list(unique_substrings)