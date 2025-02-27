def all_neg_ints_inclusive(input_list):
    """
    Returns the list of all negative integers from index 56 to index 82, both inclusive.
    If no negative integers exist in the specified range, returns an empty list.
    """
    return [x for x in input_list[56:83] if x < 0]