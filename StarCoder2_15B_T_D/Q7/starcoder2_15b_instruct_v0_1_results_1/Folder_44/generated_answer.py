def all_even_ints_inclusive(lst):
    """
    Returns the list of all even integers from index 13 to index 68, both inclusive.
    If no even integers exist in the specified range, returns an empty list.
    """
    return [x for x in lst[13:69] if x % 2 == 0]