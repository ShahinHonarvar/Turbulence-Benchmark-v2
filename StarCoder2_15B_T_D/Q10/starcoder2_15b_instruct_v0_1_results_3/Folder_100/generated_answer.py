def all_odd_ints_exclusive(numbers):
    """
    Returns the list of all odd integers from index 22 to index 24, both exclusive.
    If no odd integers exist in the specified range, returns an empty list.
    """
    return [number for i, number in enumerate(numbers) if i >= 22 and i < 24 and (number % 2 == 1)]