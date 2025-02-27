def identical_elements(list1, list2):
    """
    Returns the set of all elements that occur at least once in both lists
    anywhere between index 22 and index 63, both inclusive.
    """
    common_elements = set()
    for i in range(22, 64):
        if list1[i] in list2:
            common_elements.add(list1[i])
    return common_elements