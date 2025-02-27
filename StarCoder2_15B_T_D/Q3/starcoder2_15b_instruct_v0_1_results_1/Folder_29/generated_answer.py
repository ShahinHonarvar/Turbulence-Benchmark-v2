def all_pos_ints_inclusive(lst):
    """
    Returns the list of all positive integers from index 59 to index 97, both inclusive.
    If no positive integers exist in the specified range, an empty list is returned.
    """
    pos_ints = []
    for i in range(len(lst)):
        if i >= 59 and i <= 97:
            if lst[i] > 0:
                pos_ints.append(lst[i])
    return pos_ints