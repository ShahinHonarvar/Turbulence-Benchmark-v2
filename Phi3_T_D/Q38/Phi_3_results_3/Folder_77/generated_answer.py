from itertools import combinations

def find_subset_of_length_n(elements):
    if len(set(elements)) < 360:
        return 0
    return len(list(combinations(elements, 360)))