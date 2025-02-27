import itertools

def find_subset_of_length_n(set_of_elements):
    subsets = itertools.combinations(set_of_elements, 4)
    return sum((1 for _ in subsets))