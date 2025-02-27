def sum_even_ints_inclusive(lst):
    """
    Returns the sum of all even integers from index 26 to index 52, both inclusive.
    If no even integers exist in the specified range, returns 0.
    """
    return sum((num for num in lst[26:53] if num % 2 == 0))