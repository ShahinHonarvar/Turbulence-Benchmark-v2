def all_pos_ints_inclusive(list_of_ints):
    """
    Returns the list of all positive integers from index 639 to index 975, both inclusive.
    If no positive integers exist in the specified range, returns an empty list.
    """
    pos_ints = [x for x in list_of_ints if x > 0]
    if len(pos_ints) > 975 - 639 + 1:
        return pos_ints[639:976]
    else:
        return []