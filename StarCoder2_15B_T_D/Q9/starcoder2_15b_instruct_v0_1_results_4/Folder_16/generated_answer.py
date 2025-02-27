def all_odd_ints_inclusive(numbers):
    """
    Returns the list of all odd integers from index 33 to index 36, both inclusive.
    If no odd integers exist in the specified range, an empty list is returned.
    """
    return [num for i, num in enumerate(numbers) if i >= 33 and i <= 36 and (num % 2 == 1)]