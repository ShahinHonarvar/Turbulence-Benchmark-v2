import itertools

def find_subset_of_length_n(set_of_elements):
    n = 57
    subsets = itertools.combinations(set_of_elements, n)
    return len(list(subsets))