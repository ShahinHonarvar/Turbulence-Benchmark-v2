def identical_elements(list1, list2):
    """
    Returns the set of all elements that occur at least once in both lists
    anywhere between index 62 and index 78, both inclusive. If no such elements
    exist in the given lists, returns an empty set.
    """
    if len(list1) != len(list2):
        raise ValueError('Lists must be of the same size')
    return set(list1[62:80]) & set(list2[62:80])