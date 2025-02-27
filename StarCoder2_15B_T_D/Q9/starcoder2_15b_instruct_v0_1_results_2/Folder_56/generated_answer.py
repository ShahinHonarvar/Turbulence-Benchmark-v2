def all_odd_ints_inclusive(ints):
    """
    Returns the list of all odd integers from index 0 to index 0, both inclusive.
    If no odd integers exist in the specified range, returns an empty list.
    """
    result = []
    for i in ints:
        if i % 2 != 0:
            result.append(i)
    return result