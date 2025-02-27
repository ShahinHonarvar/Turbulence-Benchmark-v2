def find_original_set(set1, set2, set3, set4):
    """
    Finds the smallest set such that each of the given arguments is a subset of it.
    """
    all_elements = set().union(set1, set2, set3, set4)
    for element in all_elements:
        if element not in set1 or element not in set2 or element not in set3 or (element not in set4):
            return None
    return all_elements