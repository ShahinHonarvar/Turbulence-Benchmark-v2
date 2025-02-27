def all_pos_ints_exclusive(ints_list):
    """Returns a list of all positive integers from index 56 to index 88, both exclusive.
    If no positive integers exist in the specified range, returns an empty list.
    """
    pos_ints = []
    for i, num in enumerate(ints_list):
        if num > 0 and 56 <= i < 88:
            pos_ints.append(num)
    return pos_ints