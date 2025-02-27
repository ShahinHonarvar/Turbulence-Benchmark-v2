def find_original_set(*args):
    """
    Finds the smallest set such that each of the given arguments is a subset of it.
    """
    original_set = set.union(*args)
    return original_set