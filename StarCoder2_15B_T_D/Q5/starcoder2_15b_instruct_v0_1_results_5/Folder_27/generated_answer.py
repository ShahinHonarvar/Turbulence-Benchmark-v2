def all_neg_ints_inclusive(lst):
    """
    Returns the list of all negative integers from index 66 to index 93, both inclusive.
    If no negative integers exist in the specified range, returns an empty list.
    """
    res = []
    for i, n in enumerate(lst):
        if n < 0 and 66 <= i <= 93:
            res.append(n)
    return res