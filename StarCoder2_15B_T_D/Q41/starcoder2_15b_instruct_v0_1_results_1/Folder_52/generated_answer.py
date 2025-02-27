def identical_elements(list1, list2):
    """
    Returns the set of all elements that occur at least once in both lists anywhere between
    index 28 and index 38, both inclusive. If no such elements exist in the given lists,
    the function should return an empty set.
    """
    set1 = set(list1[28:39])
    set2 = set(list2[28:39])
    return set1 & set2