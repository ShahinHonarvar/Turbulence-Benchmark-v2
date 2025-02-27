def all_odd_ints_inclusive(numbers):
    """
    Returns the list of all odd integers from index 21 to index 97, both inclusive.
    If no odd integers exist in the specified range, an empty list is returned.
    """
    return [num for i, num in enumerate(numbers) if i >= 21 and i <= 97 and (num % 2 == 1)]