def all_even_ints_inclusive(numbers):
    """
    Returns the list of all even integers from index 70 to index 84, both inclusive.
    If no even integers exist in the specified range, an empty list is returned.
    """
    return [num for num in numbers[70:85] if num % 2 == 0]