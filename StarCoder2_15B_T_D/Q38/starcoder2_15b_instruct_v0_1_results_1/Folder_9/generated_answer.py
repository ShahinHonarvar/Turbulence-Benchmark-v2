import itertools

def find_subset_of_length_n(set_of_elements):
    subsets = itertools.combinations(set_of_elements, 24)
    return len(list(subsets))