def all_even_ints_inclusive(ints_list):
    """
    Returns the list of all even integers from index 35 to index 49, both inclusive.
    If no even integers exist in the specified range, an empty list is returned.
    """
    return [i for i in ints_list[35:50] if i % 2 == 0]