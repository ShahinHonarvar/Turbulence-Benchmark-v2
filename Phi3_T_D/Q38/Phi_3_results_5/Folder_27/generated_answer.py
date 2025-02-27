from itertools import combinations

def find_subset_of_length_n(elements):
    """
    Returns the number of all subsets of size 56 from the given set of elements.
    """
    return len(list(combinations(elements, 56)))