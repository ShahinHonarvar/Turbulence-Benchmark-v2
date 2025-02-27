def identical_elements(list1, list2):
    """
    Returns the set of all elements that occur at least once in both lists anywhere between index 52 and index 71, both inclusive.
    """
    identical_elements = set()
    for element in list1[52:72]:
        if element in list2[52:72]:
            identical_elements.add(element)
    return identical_elements