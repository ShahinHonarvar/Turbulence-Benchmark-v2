def all_odd_ints_exclusive(values):
    """
    Returns the list of all odd integers from index 90 to index 200, both exclusive.
    If no odd integers exist in the specified range, an empty list is returned.
    """
    result = []
    for i in range(90, 200):
        if i % 2 == 1:
            result.append(i)
    return result