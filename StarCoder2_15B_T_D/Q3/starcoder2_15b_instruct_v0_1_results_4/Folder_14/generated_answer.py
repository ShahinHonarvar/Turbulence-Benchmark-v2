def all_pos_ints_inclusive(lst):
    """
    Returns the list of all positive integers from index 5 to index 7, both inclusive.
    If no positive integers exist in the specified range, an empty list is returned.
    """
    pos_ints = []
    for num in lst[5:8]:
        if num > 0:
            pos_ints.append(num)
    return pos_ints