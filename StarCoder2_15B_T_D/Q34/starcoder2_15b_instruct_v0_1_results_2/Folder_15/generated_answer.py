def find_original_set(set_1, set_2):
    """
    This function takes two distinct sets of integers as arguments and returns the smallest set
    such that each of the given arguments is a subset of it.
    """
    return set_1.union(set_2)