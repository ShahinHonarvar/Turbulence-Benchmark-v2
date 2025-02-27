def all_odd_ints_inclusive(numbers):
    """
    Returns the list of all odd integers from index 246 to index 750, both inclusive.
    If no odd integers exist in the specified range, an empty list is returned.
    """
    return [num for i, num in enumerate(numbers) if i >= 246 and i <= 750 and (num % 2 != 0)]