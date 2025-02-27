def sum_odd_ints_inclusive(lst):
    """
    Returns the sum of all odd integers from index 639 to index 975, both inclusive.
    If no odd integers exist in the specified range, returns 0.
    """
    return sum((x for x in lst[639:976] if x % 2 == 1))