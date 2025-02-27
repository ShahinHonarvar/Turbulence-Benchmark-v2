def all_even_ints_inclusive(numbers):
    """
    Returns the list of all even integers from index 12 to index 92, both inclusive.
    If no even integers exist in the specified range, returns an empty list.
    """
    return [n for i, n in enumerate(numbers) if 12 <= i <= 92 and n % 2 == 0]