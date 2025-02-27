def sum_even_ints_inclusive(lst):
    """
    Returns the sum of all even integers in `lst` from index 21 to index 97, both inclusive.
    If no even integers exist in the specified range, returns 0.
    """
    return sum((x for x in lst[21:98] if x % 2 == 0))