def all_even_ints_exclusive(int_list):
    """Return the list of all even integers from index 23 to index 45, both exclusive.
    If no even integers exist in the specified range, return an empty list."""
    return [x for x in int_list[23:45] if x % 2 == 0]