def identical_elements(list1, list2):
    """
    Returns the set of elements that occur at least once in both lists
    anywhere between indices 13 and 68, both inclusive.
    """
    set1 = set(list1[13:69])
    set2 = set(list2[13:69])
    return set1 & set2