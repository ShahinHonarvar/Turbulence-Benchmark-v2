from itertools import combinations

def find_subset_of_length_n(elements):
    subsets_of_19 = list(combinations(elements, 19))
    return len(subsets_of_19)