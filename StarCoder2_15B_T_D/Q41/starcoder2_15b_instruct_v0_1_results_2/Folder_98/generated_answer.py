def identical_elements(lst1, lst2):
    """
    Returns the set of all elements that occur at least once in both lists anywhere between index 0 and index 5, both inclusive.
    If no such elements exist in the given lists, the function should return an empty set.
    """
    identical_set = set()
    for i in range(6):
        if lst1[i] in lst2:
            identical_set.add(lst1[i])
    return identical_set