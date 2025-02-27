def all_even_ints_inclusive(int_list):
    """Returns the list of all even integers from index 1 to index 8, both inclusive.
    If no even integers exist in the specified range, an empty list is returned."""
    return [x for x in int_list[1:9] if x % 2 == 0]