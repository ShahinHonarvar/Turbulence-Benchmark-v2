def all_odd_ints_inclusive(numbers):
    """
    Returns the list of all odd integers from index 25 to index 87, both inclusive.
    If no odd integers exist in the specified range, an empty list is returned.
    """
    return [num for i, num in enumerate(numbers) if i >= 25 and i <= 87 and (num % 2 == 1)]