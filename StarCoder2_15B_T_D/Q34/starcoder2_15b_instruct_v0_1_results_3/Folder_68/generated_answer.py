def find_original_set(set1, set2, set3):
    """
    Find the smallest set such that each of the given arguments is a subset of it.
    """
    return set1 | set2 | set3