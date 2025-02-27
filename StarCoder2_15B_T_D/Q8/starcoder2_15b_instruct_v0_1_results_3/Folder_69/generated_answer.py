def all_even_ints_exclusive(int_list):
    """
    Returns the list of all even integers from index 68 to index 99, both exclusive.
    If no even integers exist in the specified range, returns an empty list.
    """
    return [x for x in int_list[68:99] if x % 2 == 0]