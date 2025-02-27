def find_original_set(*sets):
    """
    Find the smallest set such that each of the given arguments is a subset of it.
    """
    original_set = set.union(*sets)
    return original_set