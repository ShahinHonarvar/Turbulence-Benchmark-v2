def sum_odd_ints_inclusive(lst):
    """
    Returns the sum of all odd integers in the specified range.
    """
    return sum((x for x in lst[22:64] if x % 2 != 0))