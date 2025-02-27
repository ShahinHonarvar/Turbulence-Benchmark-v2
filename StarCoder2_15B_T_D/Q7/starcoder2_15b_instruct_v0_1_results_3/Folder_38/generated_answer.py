def all_even_ints_inclusive(lst):
    """
    Returns the list of all even integers from index 22 to index 63, both inclusive.
    If no even integers exist in the specified range, returns an empty list.
    """
    return [x for i, x in enumerate(lst) if i >= 22 and i <= 63 and (x % 2 == 0)]