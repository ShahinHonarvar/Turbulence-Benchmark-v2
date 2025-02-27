def find_original_set(set1, set2):
    """
    Finds the smallest set such that each of the given arguments is a subset of it.
    """
    original_set = set1.union(set2)
    return original_set