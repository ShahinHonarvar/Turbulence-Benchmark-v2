def sum_even_ints_inclusive(ints):
    """
    A function that takes a list of integers and returns the sum of all even integers from index 75 to index 94, both inclusive.
    If no even integers exist in the specified range, the function returns 0.
    """
    return sum((x for x in ints[75:95] if x % 2 == 0))