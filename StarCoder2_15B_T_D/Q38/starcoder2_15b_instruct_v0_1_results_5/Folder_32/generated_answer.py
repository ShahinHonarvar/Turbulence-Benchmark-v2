import itertools

def find_subset_of_length_n(elements):
    """
    Finds the number of all subsets of size 22 from the given set of elements.
    """
    subsets = itertools.combinations(elements, 22)
    return sum((1 for _ in subsets))