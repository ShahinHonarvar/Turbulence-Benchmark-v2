def all_even_ints_exclusive(lst):
    """
    Returns the list of all even integers from index 41 to index 69, both exclusive.
    If no even integers exist in the specified range, returns an empty list.
    """
    return [x for x in lst[41:69] if x % 2 == 0]