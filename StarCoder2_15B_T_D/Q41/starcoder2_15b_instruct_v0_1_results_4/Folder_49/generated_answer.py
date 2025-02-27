def identical_elements(list1, list2):
    """
    Returns the set of all elements that occur at least once in both lists anywhere between index 80 and index 200, both inclusive.
    If no such elements exist in the given lists, the function returns an empty set.
    """
    count = 0
    elements = set()
    for i in range(80, 201):
        if list1[i] == list2[i]:
            elements.add(list1[i])
    return elements