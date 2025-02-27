def identical_elements(list1, list2):
    """
    Returns the set of all elements that occur at least once in both lists
    anywhere between index 37 and index 51, both inclusive. If no such elements
    exist in the given lists, returns an empty set.
    """
    return set(list1[37:52]).intersection(set(list2[37:52]))