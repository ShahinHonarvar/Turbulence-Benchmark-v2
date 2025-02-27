def all_neg_ints_inclusive(lst):
    """
    Returns the list of all negative integers from index 75 to index 94, both inclusive.
    If no negative integers exist in the specified range, an empty list is returned.
    """
    result = []
    for i, num in enumerate(lst):
        if num < 0 and 75 <= i <= 94:
            result.append(num)
    return result