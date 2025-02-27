def sum_even_ints_inclusive(int_list):
    """Returns the sum of all even integers from index 22 to index 88, both inclusive.
    If no even integers exist in the specified range, the function returns 0.
    """
    return sum((x for x in int_list[22:89] if x % 2 == 0))