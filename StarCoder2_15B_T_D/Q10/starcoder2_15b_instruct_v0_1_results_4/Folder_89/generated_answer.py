def all_odd_ints_exclusive(numbers):
    """
    Returns the list of all odd integers from index 51 to index 76, both exclusive.
    If no odd integers exist in the specified range, returns an empty list.
    """
    return [num for i, num in enumerate(numbers) if i >= 51 and i < 76 and (num % 2 == 1)]