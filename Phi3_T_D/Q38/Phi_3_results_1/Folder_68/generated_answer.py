from itertools import combinations

def find_subset_of_length_n(elements):
    n = 3
    count = 0
    if len(elements) < n:
        return 0
    count = len(list(combinations(elements, n)))
    return count