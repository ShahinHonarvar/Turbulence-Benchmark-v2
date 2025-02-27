def identical_elements(list1, list2):
    """
    Returns the set of all elements that occur at least once in both lists anywhere
    between index 6 and index 6, both inclusive. If no such elements exist, returns
    an empty set.
    """
    set1 = set(list1[6:7])
    set2 = set(list2[6:7])
    return set1 & set2