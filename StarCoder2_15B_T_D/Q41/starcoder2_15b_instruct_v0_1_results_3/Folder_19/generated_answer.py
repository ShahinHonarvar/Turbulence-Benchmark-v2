def identical_elements(list1, list2):
    """
    Returns the set of all elements that occur at least once in both lists anywhere
    between index 3 and index 5, both inclusive. If no such elements exist in the given
    lists, the function returns an empty set.
    """
    return set(list1[3:6]) & set(list2[3:6])