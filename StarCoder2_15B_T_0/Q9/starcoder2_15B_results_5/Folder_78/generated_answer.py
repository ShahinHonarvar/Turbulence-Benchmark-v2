def all_odd_ints_inclusive(numbers):
    """
    Returns the list of all odd integers from index 43 to index 51, both inclusive.
    If no odd integers exist in the specified range, an empty list is returned.
    """
    return [number for i, number in enumerate(numbers) if i >= 43 and i <= 51 and (number % 2 == 1)]