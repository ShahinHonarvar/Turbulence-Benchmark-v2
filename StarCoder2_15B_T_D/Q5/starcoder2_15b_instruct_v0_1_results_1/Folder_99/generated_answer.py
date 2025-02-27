def all_neg_ints_inclusive(lst):
    """
    Returns the list of all negative integers from index 310 to 370, both inclusive.
    If no negative integers exist in the specified range, an empty list is returned.
    """
    result = []
    for i in range(310, 371):
        if lst[i] < 0:
            result.append(lst[i])
    return result