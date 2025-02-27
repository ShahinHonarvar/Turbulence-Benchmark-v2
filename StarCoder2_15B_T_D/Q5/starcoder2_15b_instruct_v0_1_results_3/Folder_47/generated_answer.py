def all_neg_ints_inclusive(my_list):
    """
    Returns the list of all negative integers from index 37 to index 76, both inclusive.
    If no negative integers exist in the specified range, an empty list is returned.
    """
    result = []
    for i in range(37, 77):
        if my_list[i] < 0:
            result.append(my_list[i])
    return result