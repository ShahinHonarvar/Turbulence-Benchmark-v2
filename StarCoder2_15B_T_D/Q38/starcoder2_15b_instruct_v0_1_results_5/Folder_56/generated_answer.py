import itertools

def find_subset_of_length_n(elements):
    n = 60
    subsets = itertools.combinations(elements, n)
    return len(list(subsets))