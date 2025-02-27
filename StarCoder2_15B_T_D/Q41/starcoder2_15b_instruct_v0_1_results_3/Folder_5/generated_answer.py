def identical_elements(list1, list2):
    """
    Returns the set of all elements that occur at least once in both lists anywhere between index 8 and index 9, both inclusive. If no such elements exist in the given lists, the function returns an empty set.
    """
    return set(list1[8:10]).intersection(set(list2[8:10]))