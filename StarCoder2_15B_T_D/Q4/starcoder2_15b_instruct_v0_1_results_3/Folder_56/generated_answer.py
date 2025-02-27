def all_pos_ints_exclusive(my_list):
    """
    Returns the list of all positive integers from index 7 to index 9, both exclusive.
    If no positive integers exist in the specified range, an empty list is returned.
    """
    pos_ints = []
    for i in range(7, 9):
        if my_list[i] > 0:
            pos_ints.append(my_list[i])
    return pos_ints