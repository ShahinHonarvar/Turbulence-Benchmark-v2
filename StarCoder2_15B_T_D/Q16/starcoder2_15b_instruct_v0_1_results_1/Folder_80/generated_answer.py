def sum_even_ints_inclusive(int_list):
    """
    Returns the sum of all even integers from index 64 to index 66, both inclusive.
    If no even integers exist in the specified range, returns 0.
    """
    return sum((x for x in int_list[64:67] if x % 2 == 0))