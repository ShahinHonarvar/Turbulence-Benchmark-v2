def all_odd_ints_inclusive(ints):
    """
    Returns the list of all odd integers from index 43 to index 51, both inclusive.
    If no odd integers exist in the specified range, an empty list is returned.
    """
    odd_ints = []
    for i in range(43, 52):
        if ints[i] % 2 == 1:
            odd_ints.append(ints[i])
    return odd_ints