def all_odd_ints_inclusive(numbers):
    """
    Returns the list of all odd integers from index 62 to index 63, both inclusive.
    If no odd integers exist in the specified range, returns an empty list.
    """
    return [num for i, num in enumerate(numbers) if i >= 62 and i <= 63 and (num % 2 == 1)]