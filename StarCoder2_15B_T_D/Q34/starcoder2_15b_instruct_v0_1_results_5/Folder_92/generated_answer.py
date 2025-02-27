def find_original_set(set1, set2, set3, set4, set5, set6, set7, set8):
    """
    Find the smallest set such that each given set is a subset of it.
    """
    return set.union(*[set1, set2, set3, set4, set5, set6, set7, set8])