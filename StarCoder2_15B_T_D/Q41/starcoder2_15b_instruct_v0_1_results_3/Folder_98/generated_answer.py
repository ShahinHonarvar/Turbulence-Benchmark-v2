def identical_elements(list_1, list_2):
    """
    Returns the set of all elements that occur at least once in both lists anywhere between index 0 and index 5, both inclusive.
    """
    common_elements = set()
    counter = {}
    for i in range(6):
        if list_1[i] in counter:
            counter[list_1[i]] += 1
        else:
            counter[list_1[i]] = 1
        if list_2[i] in counter:
            counter[list_2[i]] += 1
        else:
            counter[list_2[i]] = 1
    for element in counter:
        if counter[element] >= 2:
            common_elements.add(element)
    return common_elements