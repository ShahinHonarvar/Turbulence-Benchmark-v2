def all_neg_ints_inclusive(lst):
    """
    Returns the list of all negative integers from index 37 to index 76, both inclusive.
    If no negative integers exist in the specified range, the function should return an empty list.
    """
    neg_ints = []
    for i in range(len(lst)):
        if lst[i] < 0 and 37 <= i <= 76:
            neg_ints.append(lst[i])
    return neg_ints