def all_odd_ints_exclusive(numbers):
    """Returns the list of all odd integers from index 18 to index 60, both exclusive.
    If no odd integers exist in the specified range, returns an empty list.

    Args:
        numbers (list): A list of integers.

    Returns:
        list: The list of all odd integers from index 18 to index 60, both exclusive.
    """
    return [num for i, num in enumerate(numbers) if i >= 18 and i < 60 and (num % 2 == 1)]