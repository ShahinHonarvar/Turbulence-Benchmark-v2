def all_neg_ints_inclusive(input_list):
    """
    Returns the list of all negative integers from index 82 to index 86, both inclusive.
    If no negative integers exist in the specified range, an empty list is returned.
    """
    return [num for i, num in enumerate(input_list) if i >= 82 and i <= 86 and (num < 0)]