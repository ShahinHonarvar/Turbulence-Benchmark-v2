def all_odd_ints_inclusive(numbers):
    """
    Returns the list of all odd integers from index 27 to index 55, both inclusive.
    If no odd integers exist in the specified range, an empty list is returned.
    """
    return [number for number in numbers[27:56] if number % 2 == 1]