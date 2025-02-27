def all_even_ints_inclusive(int_list):
    """
    Returns the list of all even integers from index 56 to index 66, both inclusive.
    If no even integers exist in the specified range, returns an empty list.
    """
    return [i for i in int_list[56:67:2] if i % 2 == 0]