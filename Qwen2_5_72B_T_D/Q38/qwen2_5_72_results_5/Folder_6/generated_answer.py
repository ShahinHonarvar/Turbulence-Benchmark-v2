from itertools import combinations

def find_subset_of_length_n(s):
    if len(s) < 89:
        return 0
    return len(list(combinations(s, 89)))