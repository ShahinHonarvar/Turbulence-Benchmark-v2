import itertools

def find_subset_of_length_n(set_of_elements):
    n = 53
    subsets = itertools.combinations(set_of_elements, n)
    num_subsets = 0
    for subset in subsets:
        num_subsets += 1
    return num_subsets