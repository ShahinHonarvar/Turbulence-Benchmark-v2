def find_original_set(*args):
    """
    Returns the smallest set that contains each of the given arguments.
    """
    smallest_set = set.union(*args)
    return smallest_set