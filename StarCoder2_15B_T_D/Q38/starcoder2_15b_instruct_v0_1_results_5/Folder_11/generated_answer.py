import itertools

def find_subset_of_length_n(elements):
    n = 77
    subsets = itertools.combinations(elements, n)
    return sum((1 for _ in subsets))