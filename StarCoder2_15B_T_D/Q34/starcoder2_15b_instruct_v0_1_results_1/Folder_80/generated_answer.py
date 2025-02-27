def find_original_set(*args):
    """
    Finds the smallest set such that each of the given arguments is a subset of it.
    """
    original_set = set()
    for arg in args:
        original_set |= arg
    return original_set