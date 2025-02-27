def all_even_ints_exclusive(lst):
    """
    Returns the list of all even integers from index 15 to index 40, both exclusive.
    If no even integers exist in the specified range, an empty list is returned.
    """
    return [num for i, num in enumerate(lst) if i >= 15 and i < 40 and (num % 2 == 0)]