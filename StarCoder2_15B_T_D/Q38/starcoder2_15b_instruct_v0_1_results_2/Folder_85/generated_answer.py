from itertools import combinations

def find_subset_of_length_n(elements):
    """
    Finds the number of all subsets of size 23 in the given set of elements.
    """
    return len(list(combinations(elements, 23)))