def identical_elements(list1, list2):
    """
    Returns the set of all elements that occur at least once in both lists
    anywhere between index 56 and index 66, both inclusive.
    """
    return set(list1[56:67]).intersection(list2[56:67])