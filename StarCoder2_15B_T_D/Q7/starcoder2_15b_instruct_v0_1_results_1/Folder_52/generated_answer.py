def all_even_ints_inclusive(my_list):
    """
    Returns the list of all even integers from index 28 to index 38, both inclusive.
    If no even integers exist in the specified range, an empty list is returned.
    """
    return [x for i, x in enumerate(my_list) if i >= 28 and i <= 38 and (x % 2 == 0)]