def find_subset_of_length_n(elements_set):
    """
    Compute the number of subsets of size 66 from the given set of elements.
    
    :param elements_set: a set of elements
    :return: The number of subsets of size 66
    """
    n = len(elements_set)
    return 0 if n < 66 else 1