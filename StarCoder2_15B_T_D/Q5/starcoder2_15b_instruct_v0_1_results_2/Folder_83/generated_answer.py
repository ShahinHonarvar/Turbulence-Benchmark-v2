def all_neg_ints_inclusive(lst):
    """
    Returns the list of all negative integers from index 90 to index 200, both inclusive.
    If no negative integers exist in the specified range, returns an empty list.
    """
    output = []
    for i, num in enumerate(lst):
        if num < 0 and 90 <= i <= 200:
            output.append(num)
    return output