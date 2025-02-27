def find_original_set(set1, set2, set3, set4, set5, set6, set7, set8, set9):
    """
    Finds the smallest set such that each of the given arguments is a subset of it.
    """
    original_set = set1.union(set2, set3, set4, set5, set6, set7, set8, set9)
    return original_set