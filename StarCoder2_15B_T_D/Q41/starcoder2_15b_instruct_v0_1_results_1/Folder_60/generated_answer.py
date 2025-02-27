def identical_elements(list1, list2):
    """
    Returns the set of all elements that occur at least once in both lists
    anywhere between index 75 and index 85, both inclusive. If no such elements
    exist in the given lists, the function should return an empty set.
    """
    set1 = set(list1[75:86])
    set2 = set(list2[75:86])
    return set1 & set2