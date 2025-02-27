def all_even_ints_exclusive(int_list):
    """
    Returns the list of all even integers from index 43 to index 99, both exclusive.
    If no even integers exist in the specified range, returns an empty list.
    """
    return [i for i in int_list[43:99] if i % 2 == 0]