def all_odd_ints_inclusive(numbers):
    """
    Returns the list of all odd integers from index 56 to index 82, both inclusive.
    If no odd integers exist in the specified range, an empty list is returned.
    """
    return [num for i, num in enumerate(numbers) if i >= 56 and i <= 82 and (num % 2 == 1)]