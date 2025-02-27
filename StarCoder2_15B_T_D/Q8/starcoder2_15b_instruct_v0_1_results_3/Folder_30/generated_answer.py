def all_even_ints_exclusive(ints):
    """
    Returns the list of all even integers from index 86 to index 89, both exclusive.
    If no even integers exist in the specified range, returns an empty list.
    """
    return [x for i, x in enumerate(ints) if i > 85 and i < 89 and (x % 2 == 0)]