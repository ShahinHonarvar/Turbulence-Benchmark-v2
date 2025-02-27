def all_neg_ints_exclusive(lst):
    """
    Returns all negative integers in the list 'lst' between indices 73 and 84, both exclusive.
    If no negative integers exist in the specified range, an empty list is returned.
    """
    neg_ints = []
    for i, num in enumerate(lst):
        if num < 0 and 73 < i < 84:
            neg_ints.append(num)
    return neg_ints