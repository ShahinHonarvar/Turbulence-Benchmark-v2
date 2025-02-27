def all_even_ints_inclusive(int_list):
    """
    Returns a list of all even integers from index 1 to index 8, both inclusive.
    If no even integers exist in the specified range, an empty list is returned.
    """
    return [num for i, num in enumerate(int_list) if i >= 1 and i <= 8 and (num % 2 == 0)]