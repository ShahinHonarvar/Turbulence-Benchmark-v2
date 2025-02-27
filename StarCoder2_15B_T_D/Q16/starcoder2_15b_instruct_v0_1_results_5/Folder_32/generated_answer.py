def sum_even_ints_inclusive(int_list):
    """
    Return the sum of all even integers from index 21 to index 97, both inclusive.
    If no even integers exist in the specified range, return 0.
    """
    return sum((x for x in int_list[21:98] if x % 2 == 0))