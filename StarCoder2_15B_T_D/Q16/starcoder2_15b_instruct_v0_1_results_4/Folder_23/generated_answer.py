def sum_even_ints_inclusive(int_list):
    """
    Returns the sum of all even integers in a list from index 52 to index 71, both inclusive.
    If no even integers exist in the specified range, returns 0.
    """
    return sum((x for x in int_list[52:72] if x % 2 == 0))