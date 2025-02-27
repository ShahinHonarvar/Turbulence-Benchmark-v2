def all_neg_ints_inclusive(integers):
    """
    Returns the list of all negative integers from index 661 to index 924, both inclusive.
    If no negative integers exist in the specified range, an empty list is returned.
    """
    filtered_integers = [x for x in integers if x < 0]
    return filtered_integers[661:925]