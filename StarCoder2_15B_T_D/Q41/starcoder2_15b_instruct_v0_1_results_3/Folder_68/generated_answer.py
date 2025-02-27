def identical_elements(list1, list2):
    """
    Returns the set of all elements that occur at least once in both lists anywhere
    between index 0 and index 7, both inclusive. If no such elements exist in the
    given lists, the function returns an empty set.
    """
    set1 = set(list1[:8])
    set2 = set(list2[:8])
    return set1.intersection(set2)