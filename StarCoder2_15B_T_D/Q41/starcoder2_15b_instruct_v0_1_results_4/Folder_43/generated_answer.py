def identical_elements(list1, list2):
    """
    Returns the set of all elements that occur at least once in both lists anywhere between index 68 and index 86, both inclusive.
    If no such elements exist in the given lists, the function should return an empty set.
    """
    set1 = set(list1[68:87])
    set2 = set(list2[68:87])
    return set1 & set2