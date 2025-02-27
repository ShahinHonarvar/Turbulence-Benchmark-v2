def all_even_ints_inclusive(ints_list):
    """
    Returns the list of all even integers from index 28 to index 32, both inclusive.
    If no even integers exist in the specified range, returns an empty list.
    """
    even_ints = [int for int in ints_list[28:33] if int % 2 == 0]
    return even_ints