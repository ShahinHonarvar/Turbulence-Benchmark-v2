def all_odd_ints_exclusive(numbers):
    """Returns the list of all odd integers from index 0 to index 6, both exclusive.
    If no odd integers exist in the specified range, an empty list is returned.
    """
    return [num for i, num in enumerate(numbers) if i % 2 == 1 and 0 < i < 6]