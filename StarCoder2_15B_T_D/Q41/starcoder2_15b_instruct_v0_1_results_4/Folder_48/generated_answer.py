def identical_elements(list1: list, list2: list) -> set:
    """
    Returns the set of all elements that occur at least once in both lists
    anywhere between index 533 and index 605, both inclusive.
    """
    return set(list1[533:606]).intersection(set(list2[533:606]))