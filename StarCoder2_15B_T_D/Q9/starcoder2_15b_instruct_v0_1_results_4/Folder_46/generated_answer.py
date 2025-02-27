def all_odd_ints_inclusive(numbers):
    """
    Returns the list of all odd integers from index 30 to index 87, both inclusive,
    or an empty list if no odd integers exist in the specified range.
    """
    return [num for i, num in enumerate(numbers) if i >= 30 and i <= 87 and (num % 2 == 1)]