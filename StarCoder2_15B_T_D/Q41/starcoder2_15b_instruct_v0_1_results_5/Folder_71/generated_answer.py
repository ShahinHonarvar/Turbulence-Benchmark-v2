def identical_elements(list1, list2):
    """
    Returns the set of all elements that occur at least once in both lists anywhere between index 26 and index 52, both inclusive. If no such elements exist in the given lists, the function should return an empty set.
    """
    set1 = {elem for i, elem in enumerate(list1) if 26 <= i <= 52}
    set2 = {elem for i, elem in enumerate(list2) if 26 <= i <= 52}
    return set1 & set2