def identical_elements(list1, list2):
    """
    Returns the set of all elements that occur at least once in both lists anywhere between
    index 5 and index 7, both inclusive. If no such elements exist in the given lists,
    returns an empty set.
    """
    set1 = set(list1[5:8])
    set2 = set(list2[5:8])
    return set1.intersection(set2)