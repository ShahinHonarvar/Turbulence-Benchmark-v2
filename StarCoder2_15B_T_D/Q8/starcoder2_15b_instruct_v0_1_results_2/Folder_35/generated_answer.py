def all_even_ints_exclusive(input_list):
    """Returns the list of all even integers from index 10 to index 79, both exclusive.
    If no even integers exist in the specified range, returns an empty list."""
    return [i for i in input_list[10:80] if i % 2 == 0]