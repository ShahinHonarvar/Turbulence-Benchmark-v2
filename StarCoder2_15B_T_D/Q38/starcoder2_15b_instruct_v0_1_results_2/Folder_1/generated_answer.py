import itertools

def find_subset_of_length_n(elements):
    subsets = itertools.combinations(elements, 85)
    return sum((1 for _ in subsets))