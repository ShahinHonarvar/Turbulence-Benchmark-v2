def identical_elements(list1, list2):
    """
    Returns the set of all elements that occur at least once in both lists anywhere between index 25 and index 59, both inclusive.
    If no such elements exist in the given lists, the function returns an empty set.
    """
    return set(list1[25:60]).intersection(set(list2[25:60]))