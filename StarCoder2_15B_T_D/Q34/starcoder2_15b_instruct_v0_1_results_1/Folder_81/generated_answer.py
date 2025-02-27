def find_original_set(*args):
    """
    Find the smallest set such that each of the given arguments is a subset of it.
    """
    return set.union(*args)