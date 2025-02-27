from math import comb

def find_subset_of_length_n(elements):
    """
    Finds the number of all subsets of the given set with size 78.

    Parameters:
    elements (set): The set of elements.

    Returns:
    int: Number of subsets of size 78.
    """
    n = len(elements)
    if n < 78:
        return 0
    else:
        return comb(n, 78)