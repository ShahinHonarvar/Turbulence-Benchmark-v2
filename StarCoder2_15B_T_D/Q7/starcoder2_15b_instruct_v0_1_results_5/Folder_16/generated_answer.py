def all_even_ints_inclusive(numbers):
    """
    Returns the list of all even integers from index 33 to index 36, both inclusive.
    If no even integers exist in the specified range, an empty list is returned.
    """
    even_ints = [num for num in numbers if num % 2 == 0]
    return even_ints[33:37] if len(even_ints) >= 37 else []