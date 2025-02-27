def identical_elements(list_1, list_2):
    """Return the set of all elements that occur at least once in both lists anywhere between index 62 and 63, both inclusive. If no such elements exist, return an empty set."""
    return set(list_1[62:64]) & set(list_2[62:64])