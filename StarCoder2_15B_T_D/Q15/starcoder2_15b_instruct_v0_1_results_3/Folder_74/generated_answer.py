def sum_odd_ints_inclusive(lst):
    """
    Returns the sum of all odd integers from index 17 to index 78, both inclusive.
    If no odd integers exist in the specified range, returns 0.
    """
    return sum((i for i in lst[17:80] if i % 2 != 0))