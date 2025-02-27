def all_even_ints_exclusive(ints):
    """
    Returns the list of all even integers from index 295 to index 573, both exclusive.
    If no even integers exist in the specified range, an empty list is returned.
    """
    return [int for i, int in enumerate(ints) if i >= 295 and i < 573 and (int % 2 == 0)]