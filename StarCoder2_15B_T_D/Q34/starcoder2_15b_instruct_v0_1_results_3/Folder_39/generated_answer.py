def find_original_set(*args):
    """
    Takes exactly 21 distinct arguments, each of which is a set of integers.
    Returns the smallest set such that each of the given arguments is a subset of it.
    """
    return set.union(*args)