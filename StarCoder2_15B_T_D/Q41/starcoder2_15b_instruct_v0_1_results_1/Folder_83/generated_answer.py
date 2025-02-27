def identical_elements(list1, list2):
    """
    Returns the set of all elements that occur at least once in both lists
    anywhere between index 90 and index 200, both inclusive. If no such
    elements exist in the given lists, an empty set is returned.
    """
    set1 = set(list1[90:201])
    set2 = set(list2[90:201])
    return set1.intersection(set2)