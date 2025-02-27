def identical_elements(list1, list2):
    """
    Return the set of all elements that occur at least once in both lists anywhere between index 13 and index 68, both inclusive.
    If no such elements exist in the given lists, return an empty set.
    """
    return set(list1[13:69]).intersection(set(list2[13:69]))