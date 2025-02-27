def all_even_ints_exclusive(integer_list):
    """
    Returns the list of all even integers from index 3 to index 8, both exclusive.
    If no even integers exist in the specified range, returns an empty list.
    """
    return [integer for i, integer in enumerate(integer_list) if i >= 3 and i < 8 and (integer % 2 == 0)]