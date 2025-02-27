def sum_odd_ints_inclusive(lst):
    """
    Returns the sum of all odd integers from index 25 to index 59, both inclusive.
    If no odd integers exist in the specified range, returns 0.
    """
    return sum((x for x in lst[25:60] if x % 2 != 0))