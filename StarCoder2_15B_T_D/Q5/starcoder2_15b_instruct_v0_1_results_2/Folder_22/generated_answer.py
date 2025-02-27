def all_neg_ints_inclusive(my_list):
    """
    Returns the list of all negative integers from index 40 to index 200, both inclusive.
    If no negative integers exist in the specified range, an empty list is returned.
    """
    result = []
    for i in range(40, 201):
        if my_list[i] < 0:
            result.append(my_list[i])
    return result