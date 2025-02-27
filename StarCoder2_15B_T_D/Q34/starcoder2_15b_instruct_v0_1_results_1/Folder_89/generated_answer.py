def find_original_set(s1, s2, s3):
    """
    Finds the smallest set such that each of the given arguments is a subset of it.
    """
    return s1.union(s2, s3)