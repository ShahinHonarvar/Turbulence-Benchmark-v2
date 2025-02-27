def identical_elements(list1, list2):
    """
    Returns the set of all elements that occur at least once in both lists anywhere between index 62 and index 92, both inclusive. If no such elements exist in the given lists, the function returns an empty set.
    """
    set1 = set(list1[62:93])
    set2 = set(list2[62:93])
    return set1 & set2