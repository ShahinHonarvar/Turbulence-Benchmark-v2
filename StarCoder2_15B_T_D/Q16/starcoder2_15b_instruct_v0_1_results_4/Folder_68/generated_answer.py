def sum_even_ints_inclusive(ints):
    """
    This function takes a list of integers and returns the sum of all even integers from index 0 to index 8, both inclusive.
    If no even integers exist in the specified range, the function returns 0.
    """
    return sum((i for i in ints[0:9] if i % 2 == 0))