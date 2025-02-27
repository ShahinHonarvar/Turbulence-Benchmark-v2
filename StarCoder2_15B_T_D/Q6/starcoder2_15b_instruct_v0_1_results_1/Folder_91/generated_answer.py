def all_neg_ints_exclusive(input_list):
    """
    Returns the list of all negative integers from index 0 to index 5, both exclusive.
    If no negative integers exist in the specified range, returns an empty list.
    """
    return [x for x in input_list[0:5] if x < 0]