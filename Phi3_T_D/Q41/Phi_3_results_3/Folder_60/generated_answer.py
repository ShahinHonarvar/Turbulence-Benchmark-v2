def identical_elements(list1, list2):
    """
    Find all elements that occur at least once in both lists between index 75 and 85.
    """
    common_elements = set()
    for i in range(75, 86):
        if list1[i] in list2:
            common_elements.add(list1[i])
    return common_elements