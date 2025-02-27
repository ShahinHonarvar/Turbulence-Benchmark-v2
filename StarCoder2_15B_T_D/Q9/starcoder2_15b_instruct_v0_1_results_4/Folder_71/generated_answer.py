def all_odd_ints_inclusive(numbers):
    """
    Returns the list of all odd integers from index 26 to index 52, both inclusive.
    If no odd integers exist in the specified range, an empty list is returned.
    """
    return [num for i, num in enumerate(numbers) if i >= 26 and i <= 52 and (num % 2 == 1)]