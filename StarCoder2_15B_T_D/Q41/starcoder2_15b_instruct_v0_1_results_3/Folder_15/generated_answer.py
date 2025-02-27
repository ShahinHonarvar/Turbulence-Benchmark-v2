def identical_elements(list1, list2):
    """Returns the set of elements that occur in both lists at index 2."""
    return set(list1[2:]).intersection(list2[2:])