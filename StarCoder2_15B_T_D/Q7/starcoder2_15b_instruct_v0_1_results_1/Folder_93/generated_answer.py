def all_even_ints_inclusive(my_list):
    """
    Returns the list of all even integers from index 75 to index 94, both inclusive.
    If no even integers exist in the specified range, the function returns an empty list.
    """
    return [x for i, x in enumerate(my_list) if i >= 75 and i <= 94 and (x % 2 == 0)]